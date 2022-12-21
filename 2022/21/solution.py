from functools import cache
from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    operations = {line.split(':')[0]: line.split(':')[1].strip().split(' ') for line in input_data.splitlines()}

    @cache
    def result(monkey: str) -> int:
        operation = operations[monkey]
        if len(operation) == 1:
            return int(operation[0])

        a, operator, b = operation

        match operator:
            case '+': return result(a) + result(b)
            case '-': return result(a) - result(b)
            case '*': return result(a) * result(b)
            case '/': return result(a) // result(b)

    @cache
    def influenced_by_human(monkey: str):
        operation = operations[monkey]
        if len(operation) == 1:
            return monkey == 'humn'

        a, _, b = operation
        return influenced_by_human(a) or influenced_by_human(b)

    @cache
    def human_input(monkey: str, expected: int) -> int:
        if monkey == 'humn':
            return expected

        a, operator, b = operations[monkey]

        if influenced_by_human(a):
            match operator:
                case '+': return human_input(a, expected - result(b))
                case '-': return human_input(a, expected + result(b))
                case '*': return human_input(a, expected // result(b))
                case '/': return human_input(a, expected * result(b))
        else:
            match operator:
                case '+': return human_input(b, expected - result(a))
                case '-': return human_input(b, result(a) - expected)
                case '*': return human_input(b, expected // result(a))
                case '/': return human_input(b, result(a) // expected)

    # Part 1
    yield result('root')

    # Part 2
    root_a, _, root_b = operations['root']
    yield human_input(root_a, result(root_b)) if influenced_by_human(root_a) else human_input(root_b, result(root_a))


run(solve)
