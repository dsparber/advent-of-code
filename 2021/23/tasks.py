from typing import Iterable

from utils import run
from utils.graph_utils import dijkstra

targets = dict(A=0, B=1, C=2, D=3)
target_positions = {k: (v + 1) * 2 for k, v in targets.items()}
costs = dict(A=1, B=10, C=100, D=1000)
allowed_hallway_positions = set(range(11)).difference(target_positions.values())


def is_empty(hallway, start, end):  # Excluding start, including end
    expected = "." * abs(end - start)
    if start < end:
        return hallway[start + 1 : end + 1] == expected
    else:
        return hallway[end:start] == expected


def next_states(current):
    hallway, levels = current

    # Move from hallway to room
    for pos, x in enumerate(hallway):
        if x in "ABCD":
            end = target_positions[x]
            if is_empty(hallway, pos, end):
                idx = targets[x]
                depth = max(
                    [depth for depth, level in enumerate(levels) if level[idx] == "."],
                    default=0,
                )
                if all([level[idx] == x for level in levels[depth + 1 :]]):
                    cost = (depth + 1 + abs(end - pos)) * costs[x]
                    new_state = (
                        hallway[:pos] + "." + hallway[pos + 1 :],
                        levels[:depth]
                        + (levels[depth][:idx] + x + levels[depth][idx + 1 :],)
                        + levels[depth + 1 :],
                    )
                    yield cost, new_state

    # Move from room to hallway
    for idx in targets.values():
        depth = (
            max(
                [depth for depth, level in enumerate(levels) if level[idx] == "."],
                default=-1,
            )
            + 1
        )
        if depth < len(levels):
            x = levels[depth][idx]
            pos = (idx + 1) * 2
            for end in allowed_hallway_positions:
                if is_empty(hallway, pos, end):
                    cost = (depth + 1 + (abs(end - pos))) * costs[x]
                    new_state = (
                        hallway[:end] + x + hallway[end + 1 :],
                        levels[:depth]
                        + (levels[depth][:idx] + "." + levels[depth][idx + 1 :],)
                        + levels[depth + 1 :],
                    )
                    yield cost, new_state


def solve(input_data: str) -> Iterable[int]:
    grid = input_data.splitlines()

    empty_hallway = "." * 11
    initial = (
        grid[2][3] + grid[2][5] + grid[2][7] + grid[2][9],
        grid[3][3] + grid[3][5] + grid[3][7] + grid[3][9],
    )

    start_1 = empty_hallway, initial
    target_1 = empty_hallway, ("ABCD",) * 2

    start_2 = empty_hallway, (initial[0], "DCBA", "DBAC", initial[1])
    target_2 = empty_hallway, ("ABCD",) * 4

    yield dijkstra(start_1, next_states, target_1)
    yield dijkstra(start_2, next_states, target_2)


run(solve)
