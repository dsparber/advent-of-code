from typing import Iterable

from utils import run
from utils.grid import Grid


def solve(input_data: str) -> Iterable[int]:
    grid = Grid.parse_char_matrix(input_data)

    positions = {grid.find("S")}
    target_steps = 6 if grid.rows == 11 else 64
    for _ in range(target_steps):
        positions = {
            neighbor
            for position in positions
            for neighbor in grid.neighbors(position)
            if grid[neighbor] != "#"
        }

    yield len(positions)


run(solve)
