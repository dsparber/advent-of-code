from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    grid = [[ord(c) - ord('a') for c in line] for line in input_data.split('\n')]

    start = 0, 0
    end = 0, 0
    lowest_points = []

    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == ord('S') - ord('a'):
                start = i, j
                grid[i][j] = 0
            if value == ord('E') - ord('a'):
                end = i, j
                grid[i][j] = ord('z') - ord('a')
            if value == 0:
                lowest_points.append((i, j))

    print(lowest_points)

    yield compute_distance(grid, start, end)
    yield min([compute_distance(grid, p, end) for p in lowest_points])


def compute_distance(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    queue = [start]
    visited = {start}
    distance = dict()
    distance[start] = 0
    while queue:
        v = queue.pop(0)
        row, col = v
        if v == end:
            break

        def possible_neighbor(neighbor: tuple[int, int]) -> bool:
            i, j = neighbor
            return 0 <= i < rows and 0 <= j < cols and grid[i][j] - 1 <= grid[row][col]

        neighbors = filter(possible_neighbor,
                           [(row + dy, col + dx) for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]])
        for n in neighbors:
            if n not in visited:
                visited.add(n)
                distance[n] = distance[v] + 1
                queue.append(n)

    if end not in distance:
        return 100000000  # Just some large numer if not reachable

    return distance[end]


run(solve)
