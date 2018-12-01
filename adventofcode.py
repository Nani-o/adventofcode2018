#!/usr/bin/env python

import os
from argparse import ArgumentParser

script_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(script_path, 'inputs')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--day', '-d', type=int, help='Day of the puzzle to run')
    parser.add_argument('--part', '-p', type=int, help='Part of the puzzle of the day to run')
    args = parser.parse_args()

    puzzle_file = "day{}".format(args.day)
    puzzle_part_func = "part{}".format(args.part)
    input_file = os.path.join(input_path, puzzle_file)

    puzzle = __import__(name=puzzle_file)
    puzzle_input = None
    with open(input_file, 'r') as f:
        puzzle_input = f.read()

    solve_func = getattr(puzzle, puzzle_part_func)
    solution = solve_func(puzzle_input)

    message = "Day {} part {} solution : {}".format(args.day, args.part, solution)
    print(message)
