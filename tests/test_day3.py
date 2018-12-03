#!/usr/bin/env python

import pytest
from aoc.day3 import part1, part2

@pytest.fixture
def input():
    return """#1 @ 1,3: 4x4
              #2 @ 3,1: 4x4
              #3 @ 5,5: 2x2"""


def test_part1(input):
    solution = part1(input)
    assert solution == 4

def test_part2(input):
    solution = part2(input)
    assert solution == 3
