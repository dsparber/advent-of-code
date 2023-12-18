from typing import Callable


def parse_char_grid_as_dict(
    input_data: str,
) -> tuple[dict[tuple[int, int], str], int, int]:
    return parse_grid_with_value_mapper_as_dict(input_data, str)


def parse_int_grid_as_dict(
    input_data: str,
) -> tuple[dict[tuple[int, int], int], int, int]:
    return parse_grid_with_value_mapper_as_dict(input_data, int)


def parse_grid_with_value_mapper_as_dict[
    T
](input_data: str, value_mapper: Callable[[str], T]) -> tuple[
    dict[tuple[int, int], T], int, int
]:
    grid = {
        (i, j): value_mapper(value)
        for i, line in enumerate(input_data.splitlines())
        for j, value in enumerate(line)
    }
    rows = max([i for i, _ in grid.keys()]) + 1
    cols = max([j for _, j in grid.keys()]) + 1

    return grid, rows, cols
