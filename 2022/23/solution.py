from collections import defaultdict
from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    elves = {(i, j) for i, row in enumerate(input_data.splitlines()) for j, v in enumerate(row) if v == '#'}

    def neighbors(pos: tuple[int, int]) -> list[tuple[int, int]]:
        i, j = pos
        deltas = {(di, dj) for di in [-1, 0, 1] for dj in [-1, 0, 1] if (di, dj) != (0, 0)}
        return [(i + di, j + dj) for di, dj in deltas]

    def move_preferences(pos: tuple[int, int]) -> list[tuple[tuple[int, int], list[tuple[int, int]]]]:
        i, j = pos
        delta_preferences = [
            ((-1, 0), [(-1, -1), (-1, 0), (-1, 1)]),  # North
            ((1, 0), [(1, -1), (1, 0), (1, 1)]),  # South
            ((0, -1), [(-1, -1), (0, -1), (1, -1)]),  # West
            ((0, 1), [(-1, 1), (0, 1), (1, 1)]),  # East
        ]
        return [((i + di, j + dj), [(i + ci, j + cj) for ci, cj in to_check_deltas])
                for (di, dj), to_check_deltas in delta_preferences]

    # Simulate rounds
    round = 0
    while True:
        targets = defaultdict(list)  # target: [elves that want to go there]
        for elf in elves:
            if all(neighbor not in elves for neighbor in neighbors(elf)):
                continue  # Elf does not move

            # Check where to move
            for i in range(4):
                move_to, to_check = move_preferences(elf)[(round + i) % 4]
                if all(pos not in elves for pos in to_check):
                    targets[move_to].append(elf)
                    break

        elves_moved = False
        for target, elves_wanting_to_go_there in targets.items():
            if len(elves_wanting_to_go_there) == 1:
                elf = elves_wanting_to_go_there[0]
                elves.remove(elf)
                elves.add(target)
                elves_moved = True

        round += 1

        if round == 10:
            rows = [i for i, _ in elves]
            cols = [j for _, j in elves]
            yield (max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1) - len(elves)

        if not elves_moved:
            yield round
            break


run(solve)
