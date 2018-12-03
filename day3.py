#!/usr/bin/env python

import re

def part1(puzzle_input):
    claims = puzzle_input.rstrip('\n').split('\n')
    all_claimed_inches = set()
    multiple_claimed_inches = set()
    for claim in claims:
        m = re.search('@ (.+),(.+): (.+)x(.+)', claim)
        start_x = int(m.group(1))
        start_y = int(m.group(2))
        len_x = int(m.group(3))
        len_y = int(m.group(4))

        # Nested loop for generating all claimed position
        for x in range(start_x, start_x + len_x):
            for y in range(start_y, start_y + len_y):
                current_inch = '{},{}'.format(x, y)
                # This inch is already appeared twice or more
                if current_inch in multiple_claimed_inches:
                    continue
                else:
                    # This inch is already appeared once
                    if current_inch in all_claimed_inches:
                        multiple_claimed_inches.add(current_inch)
                    # This inch appear for the first time
                    else:
                        all_claimed_inches.add(current_inch)
        solution = len(multiple_claimed_inches)
    return solution

def part2(puzzle_input):
    claims = puzzle_input.rstrip('\n').split('\n')
    all_claims_inches = {}
    all_claims = set()
    overlapping_claims = set()

    for claim in claims:
        m = re.search('#(.+) @ (.+),(.+): (.+)x(.+)', claim)
        id = int(m.group(1))
        start_x = int(m.group(2))
        start_y = int(m.group(3))
        len_x = int(m.group(4))
        len_y = int(m.group(5))

        all_claims.add(id)

        for x in range(start_x, start_x + len_x):
            for y in range(start_y, start_y + len_y):
                current_inch = '{},{}'.format(x, y)
                if current_inch in all_claims_inches:
                    previous_id = all_claims_inches[current_inch]
                    overlapping_claims.add(id)
                    overlapping_claims.add(previous_id)
                else:
                    all_claims_inches[current_inch] = id
    for id in all_claims:
        if id not in overlapping_claims:
            return id
