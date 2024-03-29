from typing import Callable, Iterable, Optional

from . import directions


class Grid[T]:
    def __init__(
        self,
        values: dict[tuple[int, int], T],
        rows: int,
        cols: int,
        repeats_infinitely: bool = False,
    ):
        self.values: dict[tuple[int, int], T] = values
        self.rows: int = rows
        self.cols: int = cols
        self.repeats_infinitely = repeats_infinitely

    def __getitem__(self, key: tuple[int, int]) -> T:
        if self.repeats_infinitely:
            i, j = key
            return self.values.get((i % self.rows, j % self.cols))
        return self.values.get(key)

    @property
    def max_index(self) -> tuple[int, int]:
        return self.rows - 1, self.cols - 1

    def is_within_bounds(self, index: tuple[int, int]) -> bool:
        if self.repeats_infinitely:
            return True

        i, j = index
        return 0 <= i < self.rows and 0 <= j < self.cols

    def neighbors(
        self,
        key: tuple[int, int],
        allowed_directions: Iterable[tuple[int, int]] = directions.orthogonal,
    ) -> Iterable[tuple[int, int]]:
        i, j = key
        candidates = [(i + di, j + dj) for di, dj in allowed_directions]
        return filter(self.is_within_bounds, candidates)

    def find(self, value: T, row: Optional[int] = None) -> Optional[tuple[int, int]]:
        possibilities = self.values.items()
        if row is not None:
            possibilities = (((i, j), v) for (i, j), v in possibilities if i == row)
        candidates = [k for k, v in possibilities if v == value]
        return candidates[0] if candidates else None

    def __str__(self) -> str:
        return f"Grid({self.rows}, {self.cols})"

    @staticmethod
    def parse_char_matrix(
        input_data: str, repeats_infinitely: bool = False
    ) -> "Grid[str]":
        return Grid.parse_grid_with_value_mapper(input_data, str, repeats_infinitely)

    @staticmethod
    def parse_digit_matrix(
        input_data: str, repeats_infinitely: bool = False
    ) -> "Grid[int]":
        return Grid.parse_grid_with_value_mapper(input_data, int, repeats_infinitely)

    @staticmethod
    def parse_grid_with_value_mapper[
        T
    ](
        input_data: str,
        value_mapper: Callable[[str], T],
        repeats_infinitely: bool = False,
    ) -> "Grid[T]":
        values = {
            (i, j): value_mapper(value)
            for i, line in enumerate(input_data.splitlines())
            for j, value in enumerate(line)
        }
        rows = max([i for i, _ in values.keys()]) + 1
        cols = max([j for _, j in values.keys()]) + 1

        return Grid(values, rows, cols, repeats_infinitely)
