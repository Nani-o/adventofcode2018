#!/usr/bin/env python

import pytest
from aoc.day14 import part1, part2

inputs_part1 = [9, 5, 18, 2018]

expected_part1 = [
    "5158916779",
    "0124515891",
    "9251071085",
    "5941429882"
]

@pytest.mark.parametrize("input,expected", list(zip(inputs_part1, expected_part1)))
def test_part1(input, expected):
    solution = part1(input)
    assert solution == expected
