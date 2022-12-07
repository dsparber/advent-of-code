from typing import Iterable

from utils import run

dir_sizes = list()


def parse_commands(input_data: str) -> dict:
    root = dict(children=dict())
    current = root
    for line in input_data.split("\n"):
        match line.split(" "):
            case ["$", "cd", "/"]:
                current = root
            case ["$", "cd", ".."]:
                current = current['parent']
            case ["$", "cd", name]:
                current = current['children'][name]
            case ["$", "ls"]:
                pass
            case ["dir", name]:
                current['children'][name] = dict(parent=current, children=dict())
            case [size, name]:
                current['children'][name] = int(size)
    return root


def calculate_size(dir: dict) -> int:
    match dir:
        case {'children': children}:
            dir_size = sum(map(calculate_size, children.values()))
            dir_sizes.append(dir_size)
            return dir_size
        case size:
            return size


def solve(input_data: str) -> Iterable[int]:
    root = parse_commands(input_data)
    dir_sizes.clear()
    calculate_size(root)
    yield sum([size for size in dir_sizes if size <= 100000])

    total_space = 70000000
    needed_space = 30000000
    used_space = max(dir_sizes)
    free_space = total_space - used_space
    space_to_free = needed_space - free_space
    yield min([size for size in dir_sizes if size >= space_to_free])


run(solve)
