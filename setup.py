#!/usr/bin/env python
import os
from setuptools import setup

setup(
    name = "aoc",
    version = "0.0.1",
    author = "Sofiane Medjkoune",
    description = ("A simple cli to run advent of code 2018 puzzles"),
    license = "MIT",
    keywords = "adventofcode",
    packages=['aoc'],
    entry_points = {
        'console_scripts': ['aoc=aoc.aoc:main'],
    },
)
