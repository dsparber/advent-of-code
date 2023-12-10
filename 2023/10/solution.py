from itertools import product
from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    grid = input_data.splitlines()
    start = si, sj = [(i, j) for i, l in enumerate(grid) if (j := l.find("S")) >= 0][0]

    symbol_to_directions = {
        "S": {(-1, 0), (0, 1), (1, 0), (0, -1)},
        "|": {(-1, 0), (1, 0)},
        "-": {(0, 1), (0, -1)},
        "L": {(-1, 0), (0, 1)},
        "J": {(-1, 0), (0, -1)},
        "7": {(1, 0), (0, -1)},
        "F": {(1, 0), (0, 1)},
    }

    def neighbors(node: tuple[int, int]) -> Iterable[tuple[int, int]]:
        i, j = node
        for di, dj in symbol_to_directions.get(grid[i][j], set()):
            if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
                neighbor_symbol = grid[i + di][j + dj]
                neighbor_directions = symbol_to_directions.get(neighbor_symbol, set())
                if (-di, -dj) in neighbor_directions:
                    yield i + di, j + dj

    symbol_to_directions["S"] = {(i - si, j - sj) for i, j in neighbors(start)}

    # Go from neighbor to neighbor until we arrive back at the start
    loop = {start}
    current = start
    while unvisited_neighbors := [n for n in neighbors(current) if n not in loop]:
        loop.add(current := unvisited_neighbors.pop())

    yield len(loop) // 2

    # For each coordinate that is not part of the loop, we test if it is inside
    inside_count = 0
    for i, j in product(range(len(grid)), range(len(grid[0]))):
        if (i, j) in loop:
            continue

        # In the following we count how often a straight line to the outside crosses
        # the loop.
        # From geometry, we know an odd number of crossings implies the point lies on
        # the inside of the polygon defined by the loop
        loop_crossings = 0

        j_min = j + 1
        path_to_outside = grid[i][j_min:]
        direction_from = None
        for j_k, symbol in enumerate(path_to_outside, j_min):
            if (i, j_k) not in loop:
                continue

            symbol_directions = symbol_to_directions.get(symbol, set())
            vertical = [(di, dj) for di, dj in symbol_directions if di != 0]

            # Pipe is vertical -> crosses horizontal path to outside
            if len(vertical) == 2:
                loop_crossings += 1

            # Pipe has one vertical direction, it might be start/end of a crossing
            elif len(vertical) == 1:
                direction = vertical[0]
                # We were not on a pipe before, save what direction the pipe comes from
                if direction_from is None:
                    direction_from = direction
                else:
                    # If the pipe leaves the other direction it came from, it crosses
                    if direction_from != direction:
                        loop_crossings += 1
                    direction_from = None  # Reset

        if loop_crossings % 2 == 1:
            inside_count += 1

    yield inside_count


run(solve)
