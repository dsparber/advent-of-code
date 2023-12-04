from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    grid = [[char for char in row] for row in input_data.split("\n")]

    rows = len(grid)
    cols = len(grid[0])

    def neighbors(row_col: tuple[int, int]) -> Iterable[tuple[int, int]]:
        row, col = row_col
        return [
            (row + di, col + dj)
            for di in [-1, 0, 1]
            for dj in [-1, 0, 1]
            if 0 <= row + di < rows and 0 <= col + dj < cols and not di == dj == 0
        ]

    def neighbors_of_indices(indices) -> Iterable[tuple[int, int]]:
        return {
            neighbor
            for index in indices
            for neighbor in neighbors(index)
            if neighbor not in indices
        }

    numbers = find_numbers(grid)

    total = 0
    for number, indices in numbers:
        adjacent_to_symbol = False
        for i, j in neighbors_of_indices(indices):
            if grid[i][j] != ".":
                adjacent_to_symbol = True
        if adjacent_to_symbol:
            total += number

    yield total

    total = 0
    for number_a, indices_a in numbers:
        for number_b, indices_b in numbers:
            if indices_a == indices_b:
                continue

            neighbors_a = neighbors_of_indices(indices_a)
            neighbors_b = neighbors_of_indices(indices_b)

            adjacent_to_gear = False
            for i, j in neighbors_a:
                if (i, j) in neighbors_b and grid[i][j] == "*":
                    adjacent_to_gear = True

            if adjacent_to_gear:
                total += number_a * number_b

    yield total // 2


def find_numbers(grid: list[list[str]]) -> list[tuple[int, list[tuple[int, int]]]]:
    numbers = []
    for i, row in enumerate(grid):
        number_str, indices = "", []
        for j, value in enumerate(row):
            if value.isnumeric():
                number_str += value
                indices.append((i, j))
            else:
                if indices:
                    number = int(number_str)
                    numbers.append((number, indices))
                    number_str, indices = "", []
        if indices:
            number = int(number_str)
            numbers.append((number, indices))
    return numbers


run(solve)
