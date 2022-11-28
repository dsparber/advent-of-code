import math
import re


def parse(line):
    command = line.split()[0]
    numbers = tuple(map(int, re.findall(r"-?\d+", line)))
    return command, (numbers[:2], numbers[2:4], numbers[4:])


def size(intervals):
    return math.prod([b - a + 1 if a <= b else 0 for a, b in intervals])


def intersecting_intervals(intervals_a, intervals_b):
    return [(max(a0, b0), min(a1, b1)) for (a0, a1), (b0, b1) in zip(intervals_a, intervals_b)]


def count_non_overlapping(step, remaining):
    _, intervals = step
    total = size(intervals)

    overlapping = []

    for other in remaining:
        _, other_intervals = other
        intersection = intersecting_intervals(intervals, other_intervals)
        if size(intersection) > 0:
            overlapping.append((_, intersection))

    for i in range(len(overlapping)):
        total -= count_non_overlapping(overlapping[i], overlapping[i+1:])

    return total


with open('input') as f:
    steps = [parse(line) for line in f.readlines()]

    count = 0
    for i in range(len(steps)):
        if steps[i][0] == 'on':
            count += count_non_overlapping(steps[i], steps[i+1:])

    print(count)
