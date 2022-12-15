from typing import Iterable

from utils import run
from portion import closed, Interval, CLOSED, OPEN, inf, empty


# https://github.com/AlexandreDecan/portion/issues/24#issuecomment-604456362
def discretize(i: Interval, incr: int = 1) -> Interval:
    first_step = lambda s: (OPEN, (s.lower - incr if s.left is CLOSED else s.lower), (s.upper + incr if s.right is CLOSED else s.upper), OPEN)
    second_step = lambda s: (CLOSED, (s.lower + incr if s.left is OPEN and s.lower != -inf else s.lower), (s.upper - incr if s.right is OPEN and s.upper != inf else s.upper), CLOSED)
    return i.apply(first_step).apply(second_step)


def read_line(line: str) -> list[int]:
    line = line.replace("Sensor at", "").replace(": closest beacon is at ", ", ").replace("x=", "").replace("y=", "")
    return [int(v) for v in line.split(", ")]


def solve(input_data: str) -> Iterable[int]:
    data = [read_line(line) for line in input_data.split('\n')]

    line_of_interest = 10 if data[0][0] == 2 else 2000000

    beacons_on_line = {bx for _, _, bx, by in data if by == line_of_interest}
    intervals_on_line = interval_for_line(data, line_of_interest)
    yield intervals_on_line.upper - intervals_on_line.lower + 1 - len(beacons_on_line)

    bound = 20 if data[0][0] == 2 else 4000000
    for line in range(bound + 1):
        interval = interval_for_line(data, line)
        covered_in_range = discretize(interval.intersection(closed(0, bound)))
        possible_locations = discretize(closed(0, bound) - covered_in_range)
        if not possible_locations.empty:
            x = possible_locations.lower
            yield x * 4000000 + line
            break


def interval_for_line(data: list[list[int]], line: int) -> Interval:
    intervals_on_line = empty()
    for sx, sy, bx, by in data:
        radius = abs(sx - bx) + abs(sy - by)
        distance_to_sensor = abs(sy - line)
        width = (radius - distance_to_sensor)
        interval = closed(sx - width, sx + width)
        intervals_on_line = intervals_on_line.union(interval)
    return intervals_on_line


run(solve)
