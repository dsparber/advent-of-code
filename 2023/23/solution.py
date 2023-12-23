from collections import defaultdict
from typing import Iterable

from utils import run, directions
from utils.grid import Grid


def solve(input_data: str) -> Iterable[int]:
    grid = Grid.parse_char_matrix(input_data)

    yield find_longest_path(grid)
    yield find_longest_path(grid, restrict_directions=False)


def find_longest_path(grid: Grid, restrict_directions: bool = True) -> int:
    graph = build_graph(grid, restrict_directions)

    start = grid.find(".", row=0)
    end = grid.find(".", row=grid.rows - 1)

    max_length = 0
    queue = [(start, tuple(), 0)]

    while queue:
        current, path, distance = queue.pop()

        if current == end:
            max_length = max(max_length, distance)

        for neighbor, neighbor_distance in graph[current]:
            if neighbor not in path:
                extended_path = path + (neighbor,)
                queue.append((neighbor, extended_path, distance + neighbor_distance))

    return max_length


def build_graph(grid: Grid, restrict_directions: bool) -> dict[tuple[int, int], list]:
    allowed_directions = {
        ".": directions.orthogonal,
        "<": [directions.left],
        ">": [directions.right],
        "^": [directions.up],
        "v": [directions.down],
    }
    start = grid.find(".", row=0)
    vertices = {
        vertex
        for vertex in grid.values.keys()
        if sum(grid[neighbor] != "#" for neighbor in grid.neighbors(vertex)) != 2
    }
    graph = defaultdict(list)
    queue = [(start, start, 0, False)]
    visited = set()
    while queue:
        current, root, distance, oneway = queue.pop()
        visited.add(current)

        if current in vertices:
            distance = 0
            root = current

        possible_directions = (
            allowed_directions[grid[current]]
            if restrict_directions
            else directions.orthogonal
        )
        for neighbor in grid.neighbors(current, possible_directions):
            if grid[neighbor] != "#":
                if neighbor in vertices and neighbor != root:
                    graph[root].append((neighbor, distance + 1))
                    if not restrict_directions or not oneway:
                        graph[neighbor].append((root, distance + 1))

                if neighbor not in visited:
                    queue.append(
                        (neighbor, root, distance + 1, oneway or grid[neighbor] != ".")
                    )

    return graph


run(solve)
