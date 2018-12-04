#!/usr/bin/env python

import re
from datetime import datetime

def part1(puzzle_input):
    guard_logs = sorted(puzzle_input.split('\n'))
    new_guard_pattern = re.compile("^(\[\d+-\d+-\d+ \d+:\d+\]) Guard #(\d+) begins shift")
    guard_asleep_pattern = re.compile("^(\[\d+-\d+-\d+ \d+:\d+\]) falls asleep")
    guard_wakes_pattern = re.compile("^(\[\d+-\d+-\d+ \d+:\d+\]) wakes up")

    guard_analysis = {}

    for log_entry in guard_logs:
        if new_guard_pattern.match(log_entry):
            m = new_guard_pattern.search(log_entry)
            shift_begin_date = m.group(1)
            guard_id = int(m.group(2))
            if guard_id not in guard_analysis.keys():
                guard_analysis[guard_id] = {
                    'sleep_duration': 0,
                    'sleep_wake_minutes': []
                }

        if guard_asleep_pattern.match(log_entry):
            m = guard_asleep_pattern.search(log_entry)
            sleep_begin_date = datetime.strptime(m.group(1), '[%Y-%m-%d %H:%M]')

            guard_analysis[guard_id]['sleep_wake_minutes'].append(sleep_begin_date.minute)

        if guard_wakes_pattern.match(log_entry):
            m = guard_wakes_pattern.search(log_entry)
            sleep_end_date = datetime.strptime(m.group(1), '[%Y-%m-%d %H:%M]')
            asleep_duration = (sleep_end_date - sleep_begin_date).seconds / 60
            guard_analysis[guard_id]['sleep_duration'] += asleep_duration
            guard_analysis[guard_id]['sleep_wake_minutes'].append(sleep_end_date.minute)


    minutes_asleep = 0
    for guard_id, values in guard_analysis.items():
        if values['sleep_duration'] > minutes_asleep:
            minutes_asleep = values['sleep_duration']
            guard_id_most_asleep = guard_id

    #guard_id_most_asleep = sorted(guard_analysis['sleep_duration'], key=guard_analysis['sleep_duration'].__getitem__)[0]

    minute_most_sleep = {}

    for start_minute, end_minute in zip(guard_analysis[guard_id_most_asleep]['sleep_wake_minutes'][::2], guard_analysis[guard_id_most_asleep]['sleep_wake_minutes'][1::2]):
        for minute in range(start_minute, end_minute):
            if minute in minute_most_sleep.keys():
               minute_most_sleep[minute] += 1
            else:
               minute_most_sleep[minute] = 1
    most_sleep_minute = sorted(minute_most_sleep, key=minute_most_sleep.__getitem__)[-1]
    return guard_id_most_asleep * most_sleep_minute

def part2(puzzle_input):
    guard_logs = sorted(puzzle_input.split('\n'))
    new_guard_pattern = re.compile("^(\[\d+-\d+-\d+ \d+:\d+\]) Guard #(\d+) begins shift")
    guard_asleep_pattern = re.compile("^(\[\d+-\d+-\d+ \d+:\d+\]) falls asleep")
    guard_wakes_pattern = re.compile("^(\[\d+-\d+-\d+ \d+:\d+\]) wakes up")

    guard_analysis = {}

    for log_entry in guard_logs:
        if new_guard_pattern.match(log_entry):
            m = new_guard_pattern.search(log_entry)
            shift_begin_date = m.group(1)
            guard_id = int(m.group(2))
            if guard_id not in guard_analysis.keys():
                guard_analysis[guard_id] = {
                    'sleep_duration': 0,
                    'sleep_wake_minutes': []
                }

        if guard_asleep_pattern.match(log_entry):
            m = guard_asleep_pattern.search(log_entry)
            sleep_begin_date = datetime.strptime(m.group(1), '[%Y-%m-%d %H:%M]')

            guard_analysis[guard_id]['sleep_wake_minutes'].append(sleep_begin_date.minute)

        if guard_wakes_pattern.match(log_entry):
            m = guard_wakes_pattern.search(log_entry)
            sleep_end_date = datetime.strptime(m.group(1), '[%Y-%m-%d %H:%M]')
            asleep_duration = (sleep_end_date - sleep_begin_date).seconds / 60

            guard_analysis[guard_id]['sleep_duration'] += asleep_duration
            guard_analysis[guard_id]['sleep_wake_minutes'].append(sleep_end_date.minute)


    minutes_asleep = 0
    most_frequent_minute_count = 0

    for guard_id, values in guard_analysis.items():
        guard_analysis[guard_id]['minute_count'] = {}
        for start_minute, end_minute in zip(guard_analysis[guard_id]['sleep_wake_minutes'][::2], guard_analysis[guard_id]['sleep_wake_minutes'][1::2]):
            for minute in range(start_minute, end_minute):
                if minute in guard_analysis[guard_id]['minute_count']:
                    guard_analysis[guard_id]['minute_count'][minute] += 1
                    if guard_analysis[guard_id]['minute_count'][minute] > most_frequent_minute_count:
                        most_frequent_minute_count = guard_analysis[guard_id]['minute_count'][minute]
                        most_frequent_minute = minute
                        most_frequent_guard_id = guard_id
                else:
                    guard_analysis[guard_id]['minute_count'][minute] = 1
    return most_frequent_minute * most_frequent_guard_id
