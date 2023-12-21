from operator import xor
from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    yield sum(map(valid_part_1, input_data.splitlines()))
    yield sum(map(valid_part_2, input_data.splitlines()))


def valid_part_1(line: str) -> bool:
    first_number, second_number, letter, password = parse_line(line)
    return first_number <= len([c for c in password if c == letter]) <= second_number


def valid_part_2(line: str) -> bool:
    a, b, letter, password = parse_line(line)
    return xor(password[a - 1] == letter, password[b - 1] == letter)


def parse_line(line: str) -> tuple[int, int, str, str]:
    occurrence, letter, password = line.split(" ")
    first_number, second_number = occurrence.split("-")
    return int(first_number), int(second_number), letter[0], password


run(solve)
