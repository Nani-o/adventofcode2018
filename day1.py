#!/usr/bin/env python

def part1(puzzle_input):
    frequency_changes = map(int, puzzle_input.split())
    return sum(frequency_changes)

def part2(puzzle_input):
    frequency_changes = map(int, puzzle_input.split())

    current_frequency_result = 0
    frequency_results = set([current_frequency_result])
    while True:
        for frequency_change in frequency_changes:
            current_frequency_result += frequency_change
            if current_frequency_result in frequency_results:
                return current_frequency_result
            else:
                frequency_results.add(current_frequency_result)
