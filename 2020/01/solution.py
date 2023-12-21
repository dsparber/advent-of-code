from itertools import combinations
from typing import Iterable

from math import prod

from utils import run


def solve(input_data: str) -> Iterable[int]:
    numbers = list(map(int, input_data.splitlines()))
    yield sum(a * b for a, b in combinations(numbers, 2) if a + b == 2020)
    yield sum(prod(abc) for abc in combinations(numbers, 3) if sum(abc) == 2020)


run(solve)
