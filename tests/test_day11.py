#!/usr/bin/env python

import pytest
from aoc.day11 import part1, part2, find_power_level

inputs_find_power_level = [
    (122, 79, 57),
    (217, 196, 39),
    (101, 153, 71),
]

expected_find_power_level = [-5, 0, 4]

@pytest.mark.parametrize("input,expected", list(zip(inputs_find_power_level, expected_find_power_level)))
def test_find_power_level(input, expected):
    solution = find_power_level(*input)
    assert solution == expected

inputs_part1 = [18, 42]
expected_part1 = [(33,45), (21,61)]

@pytest.mark.parametrize("input,expected", list(zip(inputs_part1, expected_part1)))
def test_part1(input, expected):
    solution = part1(input)
    assert solution == expected

inputs_part2 = [18, 42]
expected_part2 = [(90,269,16), (232,251,12)]

@pytest.mark.parametrize("input,expected", list(zip(inputs_part2, expected_part2)))
def test_part2(input, expected):
    solution = part2(input)
    assert solution == expected
