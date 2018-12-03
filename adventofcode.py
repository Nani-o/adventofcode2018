#!/usr/bin/env python

import os
import time
from argparse import ArgumentParser

script_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(script_path, 'inputs')

def get_input(day):
    input_file = os.path.join(input_path, "day{}".format(day))
    puzzle_input = None
    with open(input_file, 'r') as f:
        puzzle_input = f.read()
    return puzzle_input

def get_solver(day, part):
    puzzle_file = "day{}".format(day)
    puzzle_part_func = "part{}".format(part)

    puzzle = __import__(name=puzzle_file)
    solve_func = getattr(puzzle, puzzle_part_func)
    return solve_func

def timeit(func, arg):
    start = time.time()
    result = func(arg)
    end = time.time()
    elapsed = (end - start) * 1000
    return result, elapsed
    
def get_message(day, part, solution, elapsed):
    title = "Day {} - part {}".format(day, part)
    title = "{}\n".format(title) + "=" * len(title)
    result = "solution : {}".format(solution)
    time = "time : {0:.4f} ms".format(elapsed)

    message = "{}\n\n{}\n{}\n".format(title, result, time)
    return message

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--day', '-d', type=int, help='Day of the puzzle to run')
    parser.add_argument('--part', '-p', type=int, help='Part of the puzzle of the day to run')
    args = parser.parse_args()

    solve_func = get_solver(args.day, args.part)
    puzzle_input = get_input(args.day)
    solution, elapsed = timeit(solve_func, puzzle_input)
    
    message = get_message(args.day, args.part, solution, elapsed)
    print(message)
