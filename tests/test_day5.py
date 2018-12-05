#!/usr/bin/env python

import pytest
from aoc.day5 import part1, part2

@pytest.fixture
def input():
    return "dabAcCaCBAcCcaDA"

def test_part1(input):
    solution = part1(input)
    assert solution == 10

def test_part2(input):
    solution = part2(input)
    assert solution == 4
