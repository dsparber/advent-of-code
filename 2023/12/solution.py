from functools import cache
from typing import Iterable

from utils import run


def parse_line_part_1(line: str) -> tuple[tuple[str, ...], tuple[int, ...]]:
    pattern, target_sequence_str = line.split()
    target_sequence = tuple(map(int, target_sequence_str.split(",")))
    springs = tuple([p for p in pattern.split(".") if p])
    return springs, target_sequence


def parse_line_part_2(line: str) -> tuple[tuple[str, ...], tuple[int, ...]]:
    pattern, target_sequence_str = line.split()
    target_sequence = tuple(map(int, target_sequence_str.split(",")))
    pattern = "?".join([pattern] * 5)
    springs = tuple([p for p in pattern.split(".") if p])
    return springs, target_sequence * 5


@cache
def is_possible(spring: str, size: int) -> bool:
    if len(spring) < size:
        return False  # Spring too short
    if len(spring) > size and spring[size] == "#":
        return False  # Spring too long
    return True


@cache
def num_possibilities(
    springs: tuple[str, ...], target_sequence: tuple[int, ...]
) -> int:
    if not springs and target_sequence:
        return 0

    if not target_sequence:
        return 1 if all("#" not in spring for spring in springs) else 0

    first_spring, remaining_springs = springs[0], springs[1:]

    if not first_spring:
        return num_possibilities(remaining_springs, target_sequence)

    if first_spring[0] == "#":
        spring_size = target_sequence[0]
        if not is_possible(first_spring, spring_size):
            return 0

        remainder_of_first_spring = first_spring[spring_size:][1:]
        return num_possibilities(
            (remainder_of_first_spring, *remaining_springs),
            target_sequence[1:],
        )

    return num_possibilities(
        (first_spring[1:], *remaining_springs), target_sequence
    ) + num_possibilities((f"#{first_spring[1:]}", *remaining_springs), target_sequence)


def solve(input_data: str) -> Iterable[int]:
    total = 0
    for line in input_data.splitlines():
        springs, sequence = parse_line_part_1(line)
        total += num_possibilities(springs, sequence)
    yield total

    total = 0
    for line in input_data.splitlines():
        springs, sequence = parse_line_part_2(line)
        total += num_possibilities(springs, sequence)
    yield total


run(solve)
