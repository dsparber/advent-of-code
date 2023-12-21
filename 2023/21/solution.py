from typing import Iterable

from numpy import polyfit, polyval

from utils import run
from utils.grid import Grid


def solve(input_data: str) -> Iterable[int]:
    grid = Grid.parse_char_matrix(input_data, repeats_infinitely=True)

    is_sample = grid.rows == 11
    yield num_reachable(grid, 6 if is_sample else 64)
    yield num_reachable(grid, 26_501_365)


def num_reachable(grid: Grid, steps: int) -> int:
    start = grid.find("S")
    visited = {}
    new_positions = {start}
    num_positions = {0: 1}

    for step in range(1, grid.rows * 3):
        visited, new_positions = new_positions, {
            neighbor
            for p in new_positions
            for neighbor in grid.neighbors(p)
            if neighbor not in visited and grid[neighbor] != "#"
        }
        num_positions[step] = len(new_positions) + num_positions.get(step - 2, 0)

    n = grid.rows
    r = steps % n

    x_values = [r, n + r, 2 * n + r]

    coefficients = polyfit(x_values, [num_positions[x] for x in x_values], 2)
    return round(polyval(coefficients, steps))


run(solve)
