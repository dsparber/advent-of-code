from typing import Iterable

from utils import run


direction_vectors = dict(R=(1, 0), L=(-1, 0), U=(0, -1), D=(0, 1))


def solve(input_data: str) -> Iterable[int]:
    lines = input_data.splitlines()

    yield calculate_area(absolute_coordinates(map(parse_part_1, lines)))
    yield calculate_area(absolute_coordinates(map(parse_part_2, lines)))


def parse_part_1(line: str) -> tuple[int, int]:
    direction, distance, _ = line.split(" ")
    distance = int(distance)
    dx, dy = direction_vectors[direction]
    return distance * dx, distance * dy


def parse_part_2(line: str) -> tuple[int, int]:
    hex_value = line.split(" ")[-1][2:-1]
    distance = int(hex_value[:-1], 16)
    dx, dy = direction_vectors[{0: "R", 1: "D", 2: "L", 3: "U"}[int(hex_value[-1])]]
    return distance * dx, distance * dy


def absolute_coordinates(deltas: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    current_coordinate = 0, 0
    coordinates = [current_coordinate]
    for dx, dy in deltas:
        x, y = current_coordinate
        current_coordinate = x + dx, y + dy
        coordinates.append(current_coordinate)

    return coordinates


def calculate_area(coordinates: list[tuple[int, int]]) -> int:
    pairs = list(zip(coordinates, coordinates[1:] + [coordinates[0]]))
    circumference = sum(abs(x0 - x1) + abs(y0 - y1) for ((x0, y0), (x1, y1)) in pairs)
    area_interior = abs(sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in pairs)) // 2
    area_boundary = circumference // 2 + 1
    return area_interior + area_boundary


run(solve)
