#!/usr/bin/env python

import pytest
from aoc.day8 import part1, part2

@pytest.fixture
def input():
    return "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

def test_part1(input):
    solution = part1(input)
    assert solution == 138

def test_part2(input):
    solution = part2(input)
    assert solution == 66
