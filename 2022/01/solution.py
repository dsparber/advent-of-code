from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    calories_by_elf = [sum([int(calories) for calories in group.split('\n')]) for group in input_data.split('\n\n')]

    yield max(calories_by_elf)
    yield sum(sorted(calories_by_elf, reverse=True)[0:3])


run(solve)
