from typing import Iterable

from utils import run


score_part_1 = dict(A=dict(X=4, Y=8, Z=3), B=dict(X=1, Y=5, Z=9), C=dict(X=7, Y=2, Z=6))
score_part_2 = dict(A=dict(X=3, Y=4, Z=8), B=dict(X=1, Y=5, Z=9), C=dict(X=2, Y=6, Z=7))


def solve(input_data: str) -> Iterable[int]:
    strategy = [(line[0], line[2]) for line in input_data.split('\n')]

    yield sum(score_part_1[a][x] for a, x in strategy)
    yield sum(score_part_2[a][x] for a, x in strategy)


run(solve)
