from functools import cache
from typing import Iterable

from utils import run

valves = dict()


@cache
def max_pressure_release(open_valves: tuple[str], current: str, time: int) -> int:
    if time <= 0:
        return 0

    best_score = 0
    if current not in open_valves:
        flow = valves[current]['flow']
        if flow > 0:
            open_valves = tuple(sorted([current, *open_valves]))
            pressure_release = (time - 1) * flow
            best_score = pressure_release + max_pressure_release(open_valves, current, time - 1)

    for neighbor in valves[current]['tunnels']:
        best_score = max(best_score, max_pressure_release(open_valves, neighbor, time - 1))

    return best_score


@cache
def max_pressure_release_with_elephant(open_valves: tuple[str], current: str, time: int) -> int:
    if time <= 0:
        # Elephant is starting now
        return max_pressure_release(open_valves, "AA", 26)

    best_score = 0
    if current not in open_valves:
        flow = valves[current]['flow']
        if flow > 0:
            open_valves = tuple(sorted([current, *open_valves]))
            pressure_release = (time - 1) * flow
            best_score = pressure_release + max_pressure_release_with_elephant(open_valves, current, time - 1)

    for neighbor in valves[current]['tunnels']:
        best_score = max(best_score, max_pressure_release_with_elephant(open_valves, neighbor, time - 1))

    return best_score


def solve(input_data: str) -> Iterable[int]:
    valves.clear()
    for line in input_data.split("\n"):
        parts = line.split(" ")
        valves[parts[1]] = dict(
            flow=int(parts[4].replace("rate=", "").replace(";", "")),
            tunnels=[v.replace(",", "") for v in parts[9:]],
        )

    max_pressure_release.cache_clear()
    yield max_pressure_release(tuple(), 'AA', 30)

    max_pressure_release.cache_clear()
    max_pressure_release_with_elephant.cache_clear()
    yield max_pressure_release_with_elephant(tuple(), 'AA', 26)


run(solve)
