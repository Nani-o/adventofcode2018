#!/usr/bin/env python

import difflib
import itertools

def part1(puzzle_input):
    box_ids = puzzle_input.split()
    double_letters = 0
    triple_letters = 0

    for box_id in box_ids:
        letter_counts = set()
        unique_letters = set(box_id)
        for unique_letter in unique_letters:
            letter_count = box_id.count(unique_letter)
            letter_counts.add(letter_count)
        if 2 in letter_counts:
            double_letters += 1
        if 3 in letter_counts:
            triple_letters += 1
    checksum = double_letters * triple_letters
    return checksum

def part2(puzzle_input):
    box_ids = puzzle_input.split()
    best_ratio = 0
    for box_id1, box_id2 in itertools.combinations(box_ids, 2):
        letter_diff = 0
        for item in difflib.ndiff(box_id1, box_id2):
            if item[0] != ' ':
                letter_diff += 1
        letter_diff = letter_diff / 2
        if letter_diff == 1:
            correct_boxes = (box_id1, box_id2)
    box_id1 = correct_boxes[0]
    box_id2 = correct_boxes[1]
    correct_boxes_common_letters = ''.join([letter for idx,letter in enumerate(box_id1) if letter == box_id2[idx]])
    return correct_boxes_common_letters
