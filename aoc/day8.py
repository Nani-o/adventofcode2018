#!/usr/bin/env python

from collections import deque

def get_node(license_data):
    childs_count = license_data.popleft()
    metadata_count = license_data.popleft()
    node = {
        'childs': {},
        'metadata': []
    }
    for i in range(childs_count):
        node['childs'][i] = get_node(license_data)
    for i in range(metadata_count):
        node['metadata'].append(license_data.popleft())
    return node

def sum_nodes_metadata(node):
    childs = node['childs']
    metadatas = node['metadata']

    total = sum(metadatas)

    if len(childs) != 0:
        for child in childs.values():
            total += sum_nodes_metadata(child)
    return total

def get_node_value(node):
    childs = node['childs']
    metadatas = node['metadata']

    if len(childs) == 0:
        node_value = sum(metadatas)
    else:
        child_values = []
        for child in childs.values():
            child_values.append(get_node_value(child))
        node_value = 0
        for metadata in metadatas:
            if metadata != 0 and metadata <= len(child_values):
                node_value += child_values[metadata-1]
    return node_value

def part1(puzzle_input):
    license_data = deque(map(int, puzzle_input.rstrip('\n').split()))
    node = get_node(license_data)
    metadatas_sum = sum_nodes_metadata(node)
    return metadatas_sum

def part2(puzzle_input):
    license_data = deque(map(int, puzzle_input.rstrip('\n').split()))
    node = get_node(license_data)
    node_value = get_node_value(node)
    return node_value
