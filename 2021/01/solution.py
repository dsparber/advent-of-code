from typing import Tuple

from utils import run


def solve(input_data: str) -> Tuple[int, int]:
    numbers = [int(v) for v in input_data.split('\n')]

    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            count += 1
    yield count

    count = 0
    for i in range(1, len(numbers) - 2):
        if numbers[i+2] > numbers[i-1]:
            count += 1
    yield count


run(solve)
