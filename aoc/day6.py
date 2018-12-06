#!/usr/bin/env python

def set_input(coordinate_locations):
    minimum = {}
    maximum = {}

    locations = set()

    for location in coordinate_locations:
        x, y = [int(x) for x in location.split(', ')]

        locations.add((x, y))

        if 'x' in minimum.keys():
            if x < minimum['x']:
                minimum['x'] = x
        else:
            minimum['x'] = x
        if 'y' in minimum.keys():
            if y < minimum['y']:
                minimum['y'] = y
        else:
            minimum['y'] = y

        if 'x' in maximum.keys():
            if x > maximum['x']:
                maximum['x'] = x
        else:
            maximum['x'] = x
        if 'y' in maximum.keys():
            if y > maximum['y']:
                maximum['y'] = y
        else:
            maximum['y'] = y
    return locations, minimum, maximum

def part1(puzzle_input):
    coordinate_locations = puzzle_input.rstrip('\n').split('\n')
    locations, minimum, maximum = set_input(coordinate_locations)

    finite = set()
    infinite = set()
    for location in locations:
        current_x, current_y = location
        if minimum['x'] < current_x < maximum['x'] and minimum['y'] < current_y < maximum['y']:
            finite.add(location)
        else:
            infinite.add(location)

    shortest_distances = {}
    for x in range(minimum['x'], maximum['x'] + 1):
        for y in range(minimum['y'], maximum['y'] + 1):
            coordinate = "{},{}".format(x, y)
            shortest_distance = None
            for location in locations:
                location_x, location_y = location
                distance = abs(location_x - x) + abs(location_y - y)
                if shortest_distance == None or distance < shortest_distance:
                    shortest_location = location
                    shortest_distance = distance
                    multiple_results = False
                elif distance == shortest_distance:
                    multiple_results = True
            if not multiple_results:
                shortest_distances[coordinate] = shortest_location
    shortest_distances_count = {}
    for location in locations:
        if location in finite:
            shortest_distances_count[location] = list(shortest_distances.values()).count(location)
    return max(shortest_distances_count.values())

def part2(puzzle_input, max_total_distance=10000):
    coordinate_locations = puzzle_input.rstrip('\n').split('\n')
    locations, minimum, maximum = set_input(coordinate_locations)

    region_size = 0

    for x in range(minimum['x'], maximum['x'] + 1):
        for y in range(minimum['y'], maximum['y'] + 1):
            total_distance = 0
            for current_x, current_y in locations:
                distance = abs(x - current_x) + abs(y - current_y)
                total_distance += distance
            if total_distance < max_total_distance:
                region_size += 1
    return region_size
