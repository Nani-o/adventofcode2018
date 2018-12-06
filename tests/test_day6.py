#!/usr/bin/env python

import pytest
from aoc.day6 import part1, part2

@pytest.fixture
def input():
    return ("1, 1\n"
            "1, 6\n"
            "8, 3\n"
            "3, 4\n"
            "5, 5\n"
            "8, 9\n")

def test_part1(input):
    solution = part1(input)
    assert solution == 17

def test_part2(input):
    solution = part2(input, 32)
    assert solution == 16
