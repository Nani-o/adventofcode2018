#!/usr/bin/env python

from collections import defaultdict
import operator

def find_power_level(cell_x, cell_y, serial):
    rack_id = cell_x + 10
    power_level = (rack_id * cell_y + serial) * rack_id
    power_level = ((power_level - (power_level % 100)) % 1000)/100
    power_level = power_level - 5
    return power_level

def calculate_square_power_level(power_levels, x, y, size):
    total = 0
    x0, y0, x1, y1 = x - 1, y - 1, x + size - 1, y + size - 1
    total = power_levels[(x0, y0)] + power_levels[(x1, y1)] - power_levels[(x0, y1)] - power_levels[(x1, y0)]
    return total

def get_all_power_levels(grid_serial_number, grid_size_x, grid_size_y):
    power_levels = defaultdict(int)
    for x in range(1, grid_size_x + 1):
        for y in range(1, grid_size_y + 1):
            pl = find_power_level(x, y, grid_serial_number)
            power_levels[(x, y)] = pl + power_levels[(x-1, y)] + power_levels[(x, y-1)] - power_levels[(x-1, y-1)]
    return power_levels

def max_region(power_levels, grid_size, region_size):
    powers = {}
    for x in range(1, grid_size + 1 - region_size):
        for y in range(1, grid_size + 1 - region_size):
            region_sum = calculate_square_power_level(power_levels, x, y, region_size)
            powers[(region_sum,x,y)] = calculate_square_power_level(power_levels, x, y, region_size)

    return max(powers)

def part1(puzzle_input, grid_size_x=300, grid_size_y=300, size=3):
    grid_serial_number = int(puzzle_input)
    power_levels = get_all_power_levels(grid_serial_number, grid_size_x, grid_size_y)

    return max_region(power_levels, grid_size_x, size)[1:]

def part2(puzzle_input, grid_size_x=300, grid_size_y=300):
    grid_serial_number = int(puzzle_input)
    power_levels = get_all_power_levels(grid_serial_number, grid_size_x, grid_size_y)

    powers = []

    for s in range(1, grid_size_x):
        powers.append(max_region(power_levels, grid_size_x, s) + (s,))

    return max(powers)[1:]
