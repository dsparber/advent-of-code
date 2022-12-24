from collections import defaultdict
from functools import cache
from typing import Iterable

from utils import run


def solve(data: str) -> Iterable[int]:
    initial_grid = {(i, j): [v] for i, row in enumerate(data.splitlines()) for j, v in enumerate(row) if v != '.'}
    max_i, max_j = max(initial_grid)

    def move_blizzards(current_grid: dict[tuple[int, int], list[str]]) -> dict[tuple[int, int], list[str]]:
        updated_grid = defaultdict(list)
        for (i, j), blizzards in current_grid.items():
            for blizzard in blizzards:
                match blizzard:
                    case '#':
                        updated_grid[(i, j)].append('#')
                    case '>':
                        updated_grid[(i, j + 1) if j + 1 < max_j else (i, 1)].append(blizzard)
                    case '<':
                        updated_grid[(i, j - 1) if j - 1 > 0 else (i, max_j - 1)].append(blizzard)
                    case 'v':
                        updated_grid[(i + 1, j) if i + 1 < max_i else (1, j)].append(blizzard)
                    case '^':
                        updated_grid[(i - 1, j) if i - 1 > 0 else (max_i - 1, j)].append(blizzard)
        return updated_grid

    @cache
    def get_grid_at_time(time: int) -> dict[tuple[int, int], list[str]]:
        if time == 0:
            return initial_grid
        return move_blizzards(get_grid_at_time(time - 1))

    def duration(start: tuple[int, int], end: tuple[int, int], start_time: int) -> int:
        initial = (start, start_time)
        queue = [initial]
        visited = {initial}

        while queue:
            pos, time = queue.pop(0)
            if pos == end:
                return time

            def can_move_there(neighbor: tuple[int, int]) -> bool:
                i, j = neighbor
                next_grid = get_grid_at_time(time + 1)
                return 0 <= i <= max_i and 0 <= j <= max_j and (i, j) not in next_grid

            deltas = [(0, 0), (-1, 0), (0, -1), (0, 1), (1, 0)]
            i, j = pos
            neighbors = list(filter(can_move_there, [(i + di, j + dj) for di, dj in deltas]))
            for neighbor in neighbors:
                next_state = (neighbor, time + 1)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)

    entry = 0, 1
    exit = max_i, max_j - 1

    going_there = duration(entry, exit, 0)
    yield going_there

    going_back = duration(exit, entry, going_there)
    going_there_again = duration(entry, exit, going_back)
    yield going_there_again


run(solve)
