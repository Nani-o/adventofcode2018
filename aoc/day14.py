#!/usr/bin/env python

def part1(puzzle_input):
    recipe_numbers = int(puzzle_input)
    scores = [3, 7]
    x, y = 0, 1

    while len(scores) <= recipe_numbers + 10:
#        print("({}, {})".format(x, y))
#        print(scores)
        new_recipes = scores[x] + scores[y]
        if new_recipes >= 10:
            scores.append(1)
            scores.append(new_recipes % 10)
        else:
            scores.append(new_recipes)

        x = (x + 1 + scores[x]) % len(scores)
        y = (y + 1 + scores[y]) % len(scores)

    return ''.join([str(x) for x in scores[recipe_numbers:recipe_numbers +10]])

def part2(puzzle_input):
    return
