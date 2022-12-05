from collections import defaultdict
from typing import Iterable

from utils import run


def parse_input(input_data: str) -> tuple[list[Iterable[int]], dict[int, list[str]]]:
    stacks_str, instructions_str = input_data.split("\n\n")

    # Parse stacks
    stacks: dict[int, list[str]] = defaultdict(list)
    for line in stacks_str.split('\n')[0:-1]:
        for stack_idx in range((len(line) + 3) // 4):
            item = line[stack_idx * 4 + 1:stack_idx * 4 + 2]
            if item.strip():
                stacks[stack_idx + 1].insert(0, item)

    # Parse instructions
    instructions = [[int(v) for v in line.split(" ")[1::2]] for line in instructions_str.split("\n")]

    return instructions, stacks


def solve(input_data: str) -> Iterable[str]:
    instructions, stacks = parse_input(input_data)
    for amount, from_stack, to_stack in instructions:
        for _ in range(amount):
            stacks[to_stack].append(stacks[from_stack].pop())

    yield "".join([stacks[idx][-1] for idx in sorted(stacks.keys())])

    instructions, stacks = parse_input(input_data)
    for amount, from_stack, to_stack in instructions:
        stacks[to_stack] += stacks[from_stack][-amount:]
        stacks[from_stack] = stacks[from_stack][:-amount]

    yield "".join([stacks[idx][-1] for idx in sorted(stacks.keys())])


run(solve)
