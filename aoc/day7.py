#!/usr/bin/env python

from string import ascii_uppercase

def set_input(dependencies_log):
    dependencies = {}
    steps = set()
    for dependency_entry in dependencies_log:
        dependency, step = tuple(map(dependency_entry.split(' ').__getitem__, [1, 7]))

        if not step in dependencies.keys():
            dependencies[step] = [dependency]
        else:
            dependencies[step].append(dependency)

        for entry in step, dependency:
            if not entry in steps:
                steps.add(entry)
            if not entry in dependencies.keys():
                dependencies[entry] = []

    return steps, dependencies

def get_possible_steps(solution, dependencies):
    possible_steps = set()
    for step in dependencies:
        invalid_step = False
        if not step in solution:
            for dependency in dependencies[step]:
                if not dependency in solution:
                    invalid_step = True
            if not invalid_step:
                possible_steps.add(step)
    return possible_steps

def part1(puzzle_input):
    dependencies_log = puzzle_input.rstrip('\n').split('\n')
    steps, dependencies = set_input(dependencies_log)

    solution = ""
    while len(solution) < len(steps):
        possible_steps = get_possible_steps(solution, dependencies)
        solution += sorted(possible_steps)[0]
    return solution

def part2(puzzle_input, workers_count=5, base_time=60):
    dependencies_log = puzzle_input.rstrip('\n').split('\n')
    steps, dependencies = set_input(dependencies_log)

    solution = ""
    workers = {x: {'time': 0, 'step': ''} for x in range(workers_count)}
    seconds_elapsed = 0

    while len(solution) < len(steps):
        possible_steps = get_possible_steps(solution, dependencies)
        for possible_step in sorted(possible_steps):
            for worker, values in workers.items():
                if values['time'] == 0:
                    workers[worker]['time'] = base_time + ascii_uppercase.index(possible_step) + 1
                    workers[worker]['step'] = possible_step
                    del(dependencies[possible_step])
                    break
        available_workers = [x['time'] for x in workers.values()].count(0)
        while [x['time'] for x in workers.values()].count(0) == available_workers:
            seconds_elapsed += 1
            for worker, values in workers.items():
                time = values['time']
                if time == 1:
                    solution += values['step']
                if time != 0:
                    workers[worker]['time'] -= 1
    return seconds_elapsed
