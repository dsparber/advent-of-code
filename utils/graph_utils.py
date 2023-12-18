from heapq import heappop, heappush
from numbers import Number
from typing import Callable, Iterable, Hashable


def dijkstra[
    T: Hashable, N: Number
](
    start: T,
    get_neighbors: Callable[[T], Iterable[tuple[N, T]]],
    is_target: Callable[[T], bool],
) -> N:
    priority_queue = [(0, start)]
    distances = {start: 0}

    while priority_queue:
        distance_current, current = heappop(priority_queue)

        if distance_current > distances[current]:
            continue  # Already found a shorter path before

        if is_target(current):
            return distance_current

        for distance, neighbor in get_neighbors(current):
            d_next = distance_current + distance
            if neighbor not in distances or distances[neighbor] > d_next:
                distances[neighbor] = d_next
                heappush(priority_queue, (d_next, neighbor))

    raise AssertionError("Target unreachable")
