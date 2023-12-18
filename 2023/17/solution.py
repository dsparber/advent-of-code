from dataclasses import dataclass
from functools import partial
from typing import Iterable

from utils import run, directions
from utils.graph_utils import dijkstra
from utils.grid import Grid


def solve(input_data: str) -> Iterable[int]:
    grid = Grid.parse_digit_matrix(input_data)

    start = State(position=(0, 0), num_straights=0, direction=directions.right)

    def get_neighbors(
        state: State, min_straight: int = 0, max_straight: int = 3
    ) -> Iterable[tuple[int, State]]:
        for new_direction in directions.orthogonal:
            di, dj = new_direction
            if state.direction == (-di, -dj):
                continue  # Not allowed to go back

            is_straight = state.direction == new_direction
            if is_straight and state.num_straights >= max_straight:
                continue  # Can go straight at most max_straight times

            if not is_straight and state.num_straights < min_straight:
                continue  # Can only turn after min_straight times

            i, j = state.position
            new_position = (i + di, j + dj)
            if not grid.is_within_bounds(new_position):
                continue  # Out of bounds

            heat_loss = grid[new_position]
            yield heat_loss, State(
                position=new_position,
                direction=new_direction,
                num_straights=state.num_straights + 1 if is_straight else 1,
            )

    def is_target(state: State, min_straight: int = 0) -> bool:
        target_position = grid.max_index
        return state.position == target_position and state.num_straights >= min_straight

    yield dijkstra(start, get_neighbors, is_target)

    yield dijkstra(
        start,
        partial(get_neighbors, min_straight=4, max_straight=10),
        partial(is_target, min_straight=4),
    )


@dataclass(frozen=True, unsafe_hash=True, order=True)
class State:
    position: tuple[int, int]
    num_straights: int
    direction: tuple[int, int]


run(solve)
