from typing import Iterable

from utils import run


def update_tail(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    hx, hy = head
    tx, ty = tail

    dx, dy = hx - tx, hy - ty

    mx, my = 0, 0

    if abs(dx) >= 2 or (abs(dx) > 0 and abs(dy) >= 2):
        mx = dx // abs(dx)

    if abs(dy) >= 2 or (abs(dy) > 0 and abs(dx) >= 2):
        my = dy // abs(dy)

    return tx + mx, ty + my


def solve(input_data: str) -> Iterable[int]:
    knots: list[tuple[int, int]] = [(0, 0)] * 10

    knot_positions: list[set[tuple[int, int]]] = [set() for _ in range(10)]

    for line in input_data.split('\n'):

        head = knots[0]
        match line.split(' '):
            case ['R', n]: next_steps = [(head[0] + i, head[1]) for i in range(1, int(n) + 1)]
            case ['L', n]: next_steps = [(head[0] - i, head[1]) for i in range(1, int(n) + 1)]
            case ['U', n]: next_steps = [(head[0], head[1] + i) for i in range(1, int(n) + 1)]
            case ['D', n]: next_steps = [(head[0], head[1] - i) for i in range(1, int(n) + 1)]

        for x, y in next_steps:
            knots[0] = x, y
            knot_positions[0].add(knots[0])
            for i in range(1, 10):
                knots[i] = update_tail(knots[i-1], knots[i])
                knot_positions[i].add(knots[i])

    return len(knot_positions[1]), len(knot_positions[9])


run(solve)
