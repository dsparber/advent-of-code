from functools import cache
from typing import Iterable

from utils import run

valves = dict()


@cache
def max_pressure_release(open_valves: tuple[str], current: str, time: int, with_elephant: bool) -> int:
    if time <= 0:
        return max_pressure_release(open_valves, "AA", 26, False) if with_elephant else 0

    best_score = 0
    if current not in open_valves and valves[current]['flow'] > 0:
        open_valves = tuple(sorted([current, *open_valves]))
        pressure_release = (time - 1) * valves[current]['flow']
        best_score = pressure_release + max_pressure_release(open_valves, current, time - 1, with_elephant)

    for neighbor in valves[current]['tunnels']:
        best_score = max(best_score, max_pressure_release(open_valves, neighbor, time - 1, with_elephant))

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
    yield max_pressure_release(tuple(), 'AA', 30, False)
    yield max_pressure_release(tuple(), 'AA', 26, True)


run(solve)
