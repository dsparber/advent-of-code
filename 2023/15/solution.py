from collections import defaultdict
from functools import reduce
from typing import Iterable

from utils import run


def hash_value(value: str) -> int:
    return reduce(lambda current, char: (current + ord(char)) * 17 % 256, value, 0)


def solve(input_data: str) -> Iterable[int]:
    instructions = input_data.strip().split(",")
    yield sum(map(hash_value, instructions))

    boxes = defaultdict(list)
    lenses = dict()
    for instruction in instructions:
        if "-" in instruction:
            lens = instruction.replace("-", "")
            box_id = hash_value(lens)
            if lens in boxes[box_id]:
                boxes[box_id] = [l for l in boxes[box_id] if l != lens]
        else:
            lens, focal_length = instruction.split("=")
            lenses[lens] = int(focal_length)
            box = boxes[hash_value(lens)]
            if lens not in box:
                box.append(lens)

    yield sum(
        [
            (box_id + 1) * (box.index(lens) + 1) * focal_length
            for lens, focal_length in lenses.items()
            if lens in (box := boxes[(box_id := hash_value(lens))])
        ]
    )


run(solve)
