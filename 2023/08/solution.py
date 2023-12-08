from itertools import cycle
from math import lcm
from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    instructions, rest = input_data.split("\n\n")
    mappings = {
        line.split(" = ")[0]: line.split(" = ")[1][1:-1].split(", ")
        for line in rest.splitlines()
    }

    def cycle_length(node: str, targets: set[str]) -> int:
        count = 0
        current_node = node
        for instruction in cycle(instructions):
            current_node = mappings[current_node]["LR".index(instruction)]
            count += 1
            if current_node in targets:
                break
        return count

    yield cycle_length("AAA", {"ZZZ"}) if "AAA" in mappings else None

    starting_nodes = {n for n in mappings.keys() if n[2] == "A"}
    target_nodes = {n for n in mappings.keys() if n[2] == "Z"}
    cycle_lengths = [cycle_length(n, target_nodes) for n in starting_nodes]

    yield lcm(*cycle_lengths)


run(solve)
