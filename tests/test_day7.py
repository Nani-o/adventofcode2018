#!/usr/bin/env python

import pytest
from aoc.day7 import part1, part2

@pytest.fixture
def input():
    return ("Step C must be finished before step A can begin.\n"
            "Step C must be finished before step F can begin.\n"
            "Step A must be finished before step B can begin.\n"
            "Step A must be finished before step D can begin.\n"
            "Step B must be finished before step E can begin.\n"
            "Step D must be finished before step E can begin.\n"
            "Step F must be finished before step E can begin.\n")

def test_part1(input):
    solution = part1(input)
    assert solution == 'CABDFE'

def test_part2(input):
    solution = part2(input, 2, 0)
    assert solution == 15
