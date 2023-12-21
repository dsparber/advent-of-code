from itertools import count
from typing import Iterable

from math import prod

from utils import run
from utils.grid import Grid


def solve(input_data: str) -> Iterable[int]:
    grid = Grid.parse_char_matrix(input_data)

    yield trees_on_slope(grid, (1, 3))
    yield prod(
        trees_on_slope(grid, slope)
        for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    )


def trees_on_slope(grid: Grid, slope: tuple[int, int]) -> int:
    di, dj = slope
    return sum(
        grid[i, j % grid.cols] == "#"
        for i, j in zip(range(0, grid.rows, di), count(0, dj))
    )


run(solve)
