from itertools import product
from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    cubes = {tuple(int(c) for c in coordinates.split(',')) for coordinates in input_data.split('\n')}

    lower_bound = min(min(coordinate) for coordinate in cubes) - 1
    upper_bound = max(max(coordinate) for coordinate in cubes) + 1

    def neighbors(coordinate: tuple[int, int, int]) -> Iterable[tuple[int, int, int]]:
        x, y, z = coordinate
        for dx, dy, dz in product(*([[-1, 0, 1]] * 3)):
            neighbor = x + dx, y + dy, z + dz
            if abs(dx) + abs(dy) + abs(dz) == 1 and all([lower_bound <= c <= upper_bound for c in neighbor]):
                yield neighbor

    yield sum([6 - len(cubes.intersection(neighbors(coordinate))) for coordinate in cubes])

    surface = 0
    min_coordinate = (lower_bound, lower_bound, lower_bound)
    stack = [min_coordinate]
    outside = {min_coordinate}
    while stack:
        for neighbor in set(neighbors(stack.pop())) - outside:
            if neighbor in cubes:
                surface += 1
            else:
                outside.add(neighbor)
                stack.append(neighbor)

    yield surface


run(solve)
