from typing import Iterable

from utils import run


def common_element(lists: Iterable[str]) -> str:
    return list(set.intersection(*map(set, lists)))[0]


def priority(c: str) -> int:
    if c.isupper():
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1


def solve(input_data: str) -> Iterable[int]:
    lines = input_data.split('\n')

    chunks = [(line[0:len(line) // 2], line[len(line) // 2:]) for line in lines]
    yield sum(priority(common_element(chunk)) for chunk in chunks)

    chunks = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    yield sum(priority(common_element(chunk)) for chunk in chunks)


run(solve)
