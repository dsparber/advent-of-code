from functools import reduce
from operator import mul
from typing import Iterable

from utils import run


def analyze_tree(heights, i, j) -> tuple[bool, int]:
    height = heights[i][j]
    trees_up = [heights[i_up][j] for i_up in range(i - 1, -1, -1)]
    trees_left = [heights[i][j_left] for j_left in range(j - 1, -1, -1)]
    trees_down = [heights[i_down][j] for i_down in range(i + 1, len(heights))]
    trees_right = [heights[i][j_right] for j_right in range(j + 1, len(heights[i]))]

    trees = [trees_up, trees_left, trees_down, trees_right]

    score = reduce(mul, map(lambda t: num_visible(height, t), trees), 1)
    visible = any(map(lambda t: is_visible(height, t), trees))

    return visible, score


def num_visible(height: int, trees: list[int]) -> int:
    visible_count = 0
    for tree in trees:
        visible_count += 1
        if tree >= height:
            break
    return visible_count


def is_visible(height: int, trees: list[int]) -> bool:
    for tree in trees:
        if tree >= height:
            return False
    return True


def solve(input_data: str) -> Iterable[int]:
    trees = [[int(digit) for digit in line] for line in input_data.split('\n')]

    results: list[tuple[bool, int]] = list()
    for i, row in enumerate(trees):
        for j, value in enumerate(row):
            results.append(analyze_tree(trees, i, j))

    yield len([visible for visible, _ in results if visible])
    yield max([score for _, score in results])


run(solve)
