from itertools import combinations
from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    galaxies = [
        (i, j)
        for i, row in enumerate(input_data.splitlines())
        for j, value in enumerate(row)
        if value == "#"
    ]
    rows_with_galaxies = {i for i, _ in galaxies}
    cols_with_galaxies = {j for _, j in galaxies}

    def sum_of_distances(empty_space_size: int) -> int:
        total_distance = 0
        for (i1, j1), (i2, j2) in combinations(galaxies, 2):
            i_min, j_min = min(i1, i2), min(j1, j2)
            i_max, j_max = max(i1, i2), max(j1, j2)

            distance = 0
            for i in range(i_min, i_max):
                distance += 1 if i in rows_with_galaxies else empty_space_size
            for j in range(j_min, j_max):
                distance += 1 if j in cols_with_galaxies else empty_space_size

            total_distance += distance
        return total_distance

    yield sum_of_distances(2)
    yield sum_of_distances(1000000)


run(solve)
