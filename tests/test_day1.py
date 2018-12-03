#!/usr/bin/env python

import pytest
from aoc.day1 import part1, part2

test_inputs = [
    "+1\n-2\n+3\n+1",
    "+1\n-1",
    "+3\n+3\n+4\n-2\n-4",
    "-6\n+3\n+8\n+5\n-6",
    "+7\n+7\n-2\n-7\n-4"
]

expected_part1 = [3, 0, 4, 4, 1]
expected_part2 = [2, 0, 10, 5, 14]

@pytest.mark.parametrize("input,expected", list(zip(test_inputs, expected_part1)))
def test_part1(input, expected):
    solution = part1(input)
    assert solution == expected

@pytest.mark.parametrize("input,expected", list(zip(test_inputs, expected_part2)))
def test_part2(input, expected):
    solution = part2(input)
    assert solution == expected
