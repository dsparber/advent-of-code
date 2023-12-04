from functools import reduce
from operator import mul
from typing import Iterable

from utils import run


def parse_pair(pair_str: str) -> tuple[str, int]:
    amount_str, color = pair_str.strip().split(" ")
    return color, int(amount_str)


def parse_line(line: str) -> list[dict[str, int]]:
    _, games_str = line.split(":")
    return [
        dict([parse_pair(pair) for pair in game_str.split(",")])
        for game_str in games_str.split(";")
    ]


def is_possible(game: list[dict[str, int]]) -> bool:
    bag = dict(red=12, green=13, blue=14)
    for sample in game:
        for color, amount in sample.items():
            if bag[color] < amount:
                return False
    return True


def power_set(game: list[dict[str, int]]) -> int:
    required_cubes: dict[str, int] = dict(red=0, green=0, blue=0)
    for sample in game:
        for color, amount in sample.items():
            required_cubes[color] = max(required_cubes[color], amount)
    return reduce(mul, required_cubes.values())


def solve(input_data: str) -> Iterable[int]:
    games = list(map(parse_line, input_data.split("\n")))
    yield sum([game_id for game_id, game in enumerate(games, 1) if is_possible(game)])
    yield sum([power_set(game) for game in games])


run(solve)
