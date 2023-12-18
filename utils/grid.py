from typing import Callable


class Grid[T]:
    def __init__(self, values: dict[tuple[int, int], T], rows: int, cols: int):
        self.values: dict[tuple[int, int], T] = values
        self.rows: int = rows
        self.cols: int = cols

    def __getitem__(self, key: tuple[int, int]) -> T:
        return self.values.get(key)

    @property
    def max_index(self) -> tuple[int, int]:
        return self.rows - 1, self.cols - 1

    def is_within_bounds(self, index: tuple[int, int]) -> bool:
        i, j = index
        return 0 <= i < self.rows and 0 <= j < self.cols

    def __str__(self) -> str:
        return f"Grid({self.rows}, {self.cols})"

    @staticmethod
    def parse_char_matrix(input_data: str) -> "Grid[str]":
        return Grid.parse_grid_with_value_mapper(input_data, str)

    @staticmethod
    def parse_digit_matrix(input_data: str) -> "Grid[int]":
        return Grid.parse_grid_with_value_mapper(input_data, int)

    @staticmethod
    def parse_grid_with_value_mapper[
        T
    ](input_data: str, value_mapper: Callable[[str], T]) -> "Grid[T]":
        values = {
            (i, j): value_mapper(value)
            for i, line in enumerate(input_data.splitlines())
            for j, value in enumerate(line)
        }
        rows = max([i for i, _ in values.keys()]) + 1
        cols = max([j for _, j in values.keys()]) + 1

        return Grid(values, rows, cols)
