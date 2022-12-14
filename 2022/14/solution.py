from utils import run


def parse_input(input_data: str) -> dict[tuple[int, int], str]:
    paths = [[[int(v) for v in node.split(',')] for node in path.split(' -> ')] for path in input_data.split('\n')]
    cave: dict[tuple[int, int], str] = dict()
    for path in paths:
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    cave[(x, y)] = '#'
    return cave


def more_sand(cave: dict[tuple[int, int], str], has_floor: bool) -> bool:
    cave_depth = max([y for (_, y), v in cave.items() if v == '#'])

    if has_floor and (500, 0) in cave:
        return False

    sx, sy = 500, 0
    while True:
        if not has_floor and sy > cave_depth:
            return False

        if has_floor and sy == cave_depth + 1:
            break

        if (sx, sy + 1) not in cave:
            sy += 1
        elif (sx - 1, sy + 1) not in cave:
            sx -= 1
            sy += 1
        elif (sx + 1, sy + 1) not in cave:
            sx += 1
            sy += 1
        else:
            break

    cave[(sx, sy)] = 'o'
    return True


def count_sand(input_data: str, has_floor: bool) -> int:
    count = 0
    cave = parse_input(input_data)
    while more_sand(cave, has_floor):
        count += 1
    return count


def solve(input_data: str) -> tuple[int, int]:
    return count_sand(input_data, has_floor=False), count_sand(input_data, has_floor=True)


run(solve)
