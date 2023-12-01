from typing import Iterable

from utils import run

digit_names = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def parse_number(line: str, ignore_strings: bool = True) -> int:
    digits = []
    for i in range(len(line)):
        if line[i].isnumeric():
            digits.append(int(line[i]))
        if not ignore_strings:
            for digit, digit_name in enumerate(digit_names, 1):
                if line[i:].startswith(digit_name):
                    digits.append(digit)
    return int(f"{digits[0]}{digits[-1]}")


def solve(input_data: str) -> Iterable[int]:
    yield sum(map(parse_number, input_data.split("\n")))
    yield sum(map(lambda line: parse_number(line, False), input_data.split("\n")))


run(solve)
