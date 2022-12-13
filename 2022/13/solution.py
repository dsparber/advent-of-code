from functools import cmp_to_key
from typing import Iterable, Union

from utils import run

IntOrList = Union[int, list['IntOrList']]


def compare(a: IntOrList, b: IntOrList) -> int:

    if isinstance(a, int) and isinstance(b, int):
        return (a > b) - (a < b)

    a = a if isinstance(a, list) else [a]
    b = b if isinstance(b, list) else [b]

    for ai, bi in zip(a, b):
        compare_value = compare(ai, bi)
        if compare_value != 0:
            return compare_value

    # Ran out of elements to compare
    return compare(len(a), len(b))


def solve(input_data: str) -> Iterable[int]:
    pairs = [tuple([eval(v) for v in group.split('\n')]) for group in input_data.split('\n\n')]

    yield sum([idx for idx, (a, b) in enumerate(pairs, 1) if compare(a, b) == -1])

    divider_1, divider_2 = [[2]], [[6]]
    packets = [divider_1, divider_2] + [v for a, b in pairs for v in [a, b]]
    sorted_packets = sorted(packets, key=cmp_to_key(compare))

    yield (sorted_packets.index(divider_1) + 1) * (sorted_packets.index(divider_2) + 1)


run(solve)
