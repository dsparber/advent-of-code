from math import lcm
from typing import Iterable

from utils import run


def parse_input(input_data: str) -> list[dict]:
    monkeys = list()
    for monkey_text in input_data.split('\n\n'):
        monkey_lines = monkey_text.split("\n")
        monkeys.append(dict(
            items=eval(f"[{monkey_lines[1].split(':')[1]}]"),
            operation=monkey_lines[2].split('=')[1],
            test_divisor=int(monkey_lines[3].split(' ')[-1]),
            if_true=int(monkey_lines[4].split(' ')[-1]),
            if_false=int(monkey_lines[5].split(' ')[-1]),
            inspection_count=0
        ))
    return monkeys


def solve(input_data: str, rounds: int, worry_level_divisor: int) -> int:
    monkeys = parse_input(input_data)
    modulus = lcm(*[monkey['test_divisor'] for monkey in monkeys])
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey['items']:
                monkey['inspection_count'] += 1
                old = monkey['items'].pop(0)  # variable needed for eval
                worry_level = eval(monkey['operation']) // worry_level_divisor
                throw_to = monkey['if_true'] if worry_level % monkey['test_divisor'] == 0 else monkey['if_false']
                monkeys[throw_to]['items'].append(worry_level % modulus)

    inspection_counts = sorted([m['inspection_count'] for m in monkeys], reverse=True)
    return inspection_counts[0] * inspection_counts[1]


def solve_both(input_data: str) -> Iterable[int]:
    yield solve(input_data, 20, 3)
    yield solve(input_data, 10000, 1)


run(solve_both)
