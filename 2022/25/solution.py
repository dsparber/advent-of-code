from typing import Iterable

from utils import run


snafu_digits_to_decimal = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
decimal_to_snafu_digit = {v: k for k, v in snafu_digits_to_decimal.items()}


def to_decimal(snafu: str) -> int:
    value = 0
    for i, c in enumerate(snafu[::-1]):
        value += snafu_digits_to_decimal[c] * int(5 ** i)
    return value


def to_snafu(value: int) -> str:
    snafu = []
    while value:
        value, remainder = divmod(value, 5)
        # Adjust remainder to range -2..2
        if remainder == 3:
            value += 1
            remainder = -2
        elif remainder == 4:
            value += 1
            remainder = -1
        snafu.append(remainder)
    return "".join([decimal_to_snafu_digit[digit] for digit in reversed(snafu)])


def solve(input_data: str) -> Iterable[int]:
    yield to_snafu(sum([to_decimal(line) for line in input_data.splitlines()]))


run(solve)
