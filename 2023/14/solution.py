from itertools import product
from typing import Iterable

from utils import run

grid: list[str]


def solve(input_data: str) -> Iterable[int]:
    global grid
    grid = input_data.splitlines()
    initial = {
        (i, j)
        for i, row in enumerate(grid)
        for j, value in enumerate(row)
        if value == "O"
    }

    yield weight(move_direction((-1, 0), initial))
    yield weight(move_cycles(initial, 1000000000))


def move_cycles(initial, total_cycles: int):
    current = initial
    known_states = dict()
    cycle = 0
    cycle_length = None
    while cycle < total_cycles:
        state = tuple(current)
        if state in known_states and cycle_length is None:
            cycle_length = cycle - known_states[state]
            cycle += cycle_length * ((total_cycles - cycle) // cycle_length)
        else:
            known_states[state] = cycle
            current = move_cycle(current)
            cycle += 1
    return current


def move_cycle(initial: set[tuple[int, int]]) -> set[tuple[int, int]]:
    current = initial
    for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        current = move_direction(direction, current)
    return current


def move_direction(
    direction: tuple[int, int], initial: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    current = initial
    while (updated := move_one_step(direction, current)) != current:
        current = updated
    return current


def move_one_step(
    direction: tuple[int, int], initial: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    rows, cols = len(grid), len(grid[0])
    di, dj = direction
    si = 1 if di >= 0 else -1
    sj = 1 if dj >= 0 else -1
    updated = set()
    for i, j in product(range(rows)[::si], range(cols)[::sj]):
        if (i, j) in initial:
            k, l = i + di, j + dj
            within_bounds = 0 <= k < rows and 0 <= l < cols
            if not within_bounds or grid[k][l] == "#" or (k, l) in initial:
                updated.add((i, j))
            else:
                updated.add((k, l))

    return updated


def weight(positions: set[tuple[int, int]]) -> int:
    rows = len(grid)
    return sum(rows - i for i, _ in positions)


run(solve)
