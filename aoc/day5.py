#!/usr/bin/env python

import re
from string import ascii_lowercase

def get_regex():
    regex_pattern = []
    for letter in ascii_lowercase:
        regex_pattern.append(letter + letter.upper())
        regex_pattern.append(letter.upper() + letter)
    regex_pattern = "|".join(regex_pattern)
    return re.compile(regex_pattern)

def reacting_polymer(polymer):
    regex = get_regex()
    while True:
        solution = regex.sub('', polymer)
        if len(polymer) == len(solution):
            break
        polymer = solution
    return solution

def part1(puzzle_input):
    puzzle_input = puzzle_input.strip('\n')

    polymer_reacted = reacting_polymer(puzzle_input)

    return len(polymer_reacted)

def part2(puzzle_input):
    puzzle_input = puzzle_input.strip('\n')
    shortest_polymer = puzzle_input
    unique_letters_ignorecase = set(puzzle_input.lower())

    for letter in unique_letters_ignorecase:
        puzzle_copy = puzzle_input
        puzzle_copy = puzzle_copy.replace(letter, '')
        puzzle_copy = puzzle_copy.replace(letter.upper(), '')
        polymer_reacted = reacting_polymer(puzzle_copy)
        if len(polymer_reacted) < len(shortest_polymer):
            shortest_polymer = polymer_reacted

    return len(shortest_polymer)
