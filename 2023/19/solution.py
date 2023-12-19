from typing import Iterable

from math import prod

from utils import run


def solve(input_data: str) -> Iterable[int]:
    workflows_block, parts_block = input_data.split("\n\n")
    workflows = dict(map(parse_workflow, workflows_block.splitlines()))
    parts = list(map(parse_part, parts_block.splitlines()))

    accepting_constraints = find_accepting_constraints(workflows)
    accepting_bounds = list(map(bounds_for_constraints, accepting_constraints))

    yield sum([sum(p.values()) for p in parts if accepted(p, accepting_bounds)])
    yield sum(map(num_possibilities, accepting_bounds))


def parse_workflow(line: str) -> tuple[str, list[str]]:
    rules_start = line.index("{")
    name = line[:rules_start]
    rules = line[rules_start + 1 : -1].split(",")
    return name, rules


def parse_part(line: str) -> dict[str, int]:
    return {_.split("=")[0]: int(_.split("=")[1]) for _ in line[1:-1].split(",")}


def find_accepting_constraints(workflows: dict[str, list[str]]) -> list[list[str]]:
    accepting_constraints = []
    queue = [("in", [])]
    while queue:
        current, constraints = queue.pop(0)
        if current == "A":
            accepting_constraints.append(constraints)
            continue
        if current != "R":
            for rule in workflows[current]:
                if ":" in rule:
                    constraint, next_workflow = rule.split(":")
                    queue.append((next_workflow, constraints + [constraint]))
                    constraints += [complement(constraint)]
                else:
                    queue.append((rule, constraints))

    return accepting_constraints


def complement(constraint: str) -> str:
    if ">" in constraint:
        variable, bound = constraint.split(">")
        return f"{variable}<{int(bound) + 1}"

    variable, bound = constraint.split("<")
    return f"{variable}>{int(bound) - 1}"


def bounds_for_constraints(constraints: list[str]) -> dict[str, tuple[int, int]]:
    variables = "xmas"
    lower_bounds = {variable: [1] for variable in variables}
    upper_bounds = {variable: [4000] for variable in variables}
    for constraint in constraints:
        if ">" in constraint:
            variable, bound = constraint.split(">")
            lower_bounds[variable].append(int(bound) + 1)
        if "<" in constraint:
            variable, bound = constraint.split("<")
            upper_bounds[variable].append(int(bound) - 1)

    return {k: (max(lower_bounds[k]), min(upper_bounds[k])) for k in variables}


def num_possibilities(bounds: dict[str, tuple[int, int]]) -> int:
    return prod([upper - lower + 1 for lower, upper in bounds.values()])


def accepted(part: dict[str, int], bounds: list[dict[str, tuple[int, int]]]) -> bool:
    return any(map(lambda bound: within_bound(bound, part), bounds))


def within_bound(bound: dict[str, tuple[int, int]], part: dict[str, int]) -> bool:
    for variable, value in part.items():
        lower, upper = bound[variable]
        if not (lower <= value <= upper):
            return False
    return True


run(solve)
