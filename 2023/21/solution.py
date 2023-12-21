from typing import Iterable

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

    # Decompose: steps = kn + r
    n = grid.rows
    k, r = steps // n, steps % n

    positions_1n_r = num_positions[n + r]
    positions_2n_r = num_positions[2 * n + r]
    d1 = positions_2n_r - positions_1n_r
    d2 = positions_2n_r + num_positions[r] - 2 * positions_1n_r

    return positions_2n_r + (k - 2) * (d1 + (k - 1) * d2 // 2)


run(solve)
