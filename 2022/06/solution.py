from typing import Iterable

from utils import run


def find_marker(message: str, length: int) -> int:
    for i in range(len(message)):
        if len(set(message[i:i + length])) == length:
            return i + length


def solve(input_data: str) -> Iterable[int]:
    return find_marker(input_data, 4), find_marker(input_data, 14)


run(solve)
