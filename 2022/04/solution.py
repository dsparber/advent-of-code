from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    intervals = [[[int(v) for v in interval.split('-')] for interval in line.split(',')]
                 for line in input_data.split('\n')]

    contained = 0
    overlapping = 0
    for (a, b), (c, d) in intervals:
        first_set = set(range(a, b + 1))
        second_set = set(range(c, d + 1))
        intersection_size = len(first_set.intersection(second_set))
        if intersection_size > 0:
            overlapping += 1
        if intersection_size == min(len(first_set), len(second_set)):
            contained += 1
    return contained, overlapping


run(solve)
