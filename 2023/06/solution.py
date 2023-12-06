import re
from functools import reduce
from math import sqrt, ceil, floor
from operator import mul
from typing import Iterable

from utils import run


def wins(t: int, d: int) -> int:
    # Quick math: solved quadratic equation x (t - x) = d on paper
    a = 0.5 * (t - sqrt(t**2 - 4 * d))
    b = 0.5 * (t + sqrt(t**2 - 4 * d))
    epsilon = 0.1  # Since we need to be strictly better than d
    return floor(b - epsilon) - ceil(a + epsilon) + 1


def solve(input_data: str) -> Iterable[int]:
    times, distances = [
        list(map(int, re.split(r"\s+", line)[1:])) for line in input_data.split("\n")
    ]
    yield reduce(mul, [wins(t, d) for t, d in zip(times, distances)], 1)

    time, distance = [int("".join(map(str, numbers))) for numbers in [times, distances]]
    yield wins(time, distance)


run(solve)
