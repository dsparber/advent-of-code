from typing import Iterable

from portion import Interval, singleton, closed

from utils import run
from utils.interval_utils import discretize_interval, offset_interval


def solve(input_data: str) -> Iterable[int]:
    seeds = list(map(int, input_data.split("\n")[0].split(":")[1].strip().split(" ")))
    maps = [
        [list(map(int, line.split(" "))) for line in block.split("\n")[1:]]
        for block in input_data.split("\n\n")[1:]
    ]

    def compute_location(interval: Interval) -> int:
        for map_definition in maps:

            def transform(original: Interval) -> Interval:
                identity = original
                mapped_intervals = Interval()

                for map_entry in map_definition:
                    destination_start, source_start, length = map_entry
                    source_interval = closed(source_start, source_start + length - 1)

                    # Subtract source interval from identity
                    identity = discretize_interval(identity - source_interval)

                    # Offset relevant part of interval, add to mapped intervals
                    mapped_intervals |= offset_interval(
                        source_interval.intersection(original),
                        destination_start - source_start,
                    )

                return mapped_intervals.union(identity)

            interval = transform(interval)

        return interval.lower

    interval_for_seeds = Interval(*map(singleton, seeds))
    interval_for_seed_ranges = Interval(
        *[closed(start, start + n - 1) for start, n in zip(seeds[::2], seeds[1::2])]
    )

    yield compute_location(interval_for_seeds)
    yield compute_location(interval_for_seed_ranges)


run(solve)
