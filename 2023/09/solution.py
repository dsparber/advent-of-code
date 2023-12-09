from typing import Iterable

from utils import run


def extrapolate_last(numbers: list[int]) -> int:
    if all([number == 0 for number in numbers]):
        return 0

    differences = [b - a for a, b in zip(numbers, numbers[1:])]
    return numbers[-1] + extrapolate_last(differences)


def extrapolate_first(numbers: list[int]) -> int:
    if all([number == 0 for number in numbers]):
        return 0

    differences = [b - a for a, b in zip(numbers, numbers[1:])]
    return numbers[0] - extrapolate_first(differences)


def solve(input_data: str) -> Iterable[int]:
    sequences = [list(map(int, line.split(" "))) for line in input_data.splitlines()]
    yield sum(map(extrapolate_last, sequences))
    yield sum(map(extrapolate_first, sequences))


run(solve)
