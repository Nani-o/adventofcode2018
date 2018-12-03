#!/usr/bin/env python

import pytest
from aoc.day2 import part1, part2

def test_part1():
    input = """abcdef
               bababc
               abbcde
               abcccd
               aabcdd
               abcdee
               ababab"""
    solution = part1(input)
    assert solution == 12

def test_part2():
    input = """abcde
               fghij
               klmno
               pqrst
               fguij
               axcye
               wvxyz"""
    solution = part2(input)
    assert solution == "fgij"
