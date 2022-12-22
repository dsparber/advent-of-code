from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    grid_str, commands_str = input_data.split('\n\n')
    grid = grid_str.splitlines()
    commands = commands_str.replace('R', ',R,').replace('L', ',L,').split(',')

    pos = 0, grid[0].index('.')
    facing = 0

    def get_next_pos(pos: tuple[int, int], facing: int) -> tuple[int, int]:
        i, j = pos
        row: str = grid[i]
        col: str = "".join([r[j] if j < len(r) else ' ' for r in grid])
        match facing:
            case 0:  # right
                if j + 1 >= len(row) or row[j + 1] == ' ':
                    return i, min(row.index('.'), row.index('#'))
                return i, j + 1
            case 1:  # down
                if i + 1 >= len(col) or col[i + 1] == ' ':
                    return min(col.index('.'), col.index('#')), j
                return i + 1, j
            case 2:  # left
                if j <= 0 or row[j - 1] == ' ':
                    return i, max(row.rindex('.'), row.rindex('#'))
                return i, j - 1
            case 3:  # up
                if i <= 0 or col[i - 1] == ' ':
                    return max(col.rindex('.'), col.rindex('#')), j
                return i - 1, j

    for command in commands:
        match command:
            case 'R': facing = (facing + 1) % 4
            case 'L': facing = (facing - 1) % 4
            case amount_str:
                amount = int(amount_str)
                for _ in range(amount):
                    next_row, next_col = get_next_pos(pos, facing)
                    if grid[next_row][next_col] != '.':
                        print(grid[next_row][next_col])
                        break
                    pos = next_row, next_col

    i, j = pos
    yield 1000 * (i + 1) + 4 * (j + 1) + facing


run(solve)
