from collections import defaultdict
from typing import Iterable

from utils import run

up = -1, 0
down = 1, 0
left = 0, -1
right = 0, 1


def new_directions(symbol: str, direction: tuple[int, int]) -> list[tuple[int, int]]:
    match symbol:
        case "-" if direction in {up, down}:
            return [left, right]
        case "|" if direction in {left, right}:
            return [up, down]
        case "/":
            if direction == up:
                return [right]
            if direction == down:
                return [left]
            if direction == left:
                return [down]
            if direction == right:
                return [up]
        case "\\":
            if direction == up:
                return [left]
            if direction == down:
                return [right]
            if direction == left:
                return [up]
            if direction == right:
                return [down]

    return [direction]


def solve(input_data: str) -> Iterable[int]:
    grid = {
        (i, j): symbol
        for i, line in enumerate(input_data.splitlines())
        for j, symbol in enumerate(line)
    }
    rows = max([i for i, _ in grid.keys()]) + 1
    cols = max([j for _, j in grid.keys()]) + 1

    def solve_for_start(start: tuple[tuple[int, int], tuple[int, int]]) -> int:
        tiles_directions = defaultdict(list)
        beams_to_trace = [start]
        while beams_to_trace:
            tile, direction = beams_to_trace.pop()

            for new_direction in new_directions(grid[tile], direction):
                if new_direction not in tiles_directions[tile]:
                    tiles_directions[tile].append(new_direction)
                    i, j = tile
                    di, dj = new_direction
                    if 0 <= i + di < rows and 0 <= j + dj < cols:
                        beams_to_trace.append(((i + di, j + dj), new_direction))

        return len(tiles_directions.keys())

    # visualize_grid(cols, grid, rows, tiles_directions)

    yield solve_for_start(((0, 0), right))

    possible_starts = (
        [((i, 0), right) for i in range(rows)]
        + [((i, cols - 1), left) for i in range(rows)]
        + [((0, j), down) for j in range(cols)]
        + [((rows - 1, j), up) for j in range(cols)]
    )
    yield max(map(solve_for_start, possible_starts))


def visualize_grid(cols, grid, rows, tiles_directions):
    string = ""
    for i in range(rows):
        string += "\n"
        for j in range(cols):
            if (i, j) in tiles_directions:
                length = len(tiles_directions[i, j])
                if length == 1:
                    direction = tiles_directions[i, j][0]
                    if direction == up:
                        string += "^"
                    if direction == down:
                        string += "v"
                    if direction == left:
                        string += "<"
                    if direction == right:
                        string += ">"
                else:
                    string += str(length)
            else:
                string += grid[(i, j)]
    print(string)


run(solve)
