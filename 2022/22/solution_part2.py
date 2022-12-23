from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    grid_str, commands_str = input_data.split('\n\n')

    commands = commands_str.replace('R', ',R,').replace('L', ',L,').split(',')
    tiles = {(i, j): v for i, row in enumerate(grid_str.splitlines(), 1) for j, v in enumerate(row, 1) if v != ' '}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    pos = min(tiles.keys())
    facing = 0
    for command in commands:
        match command:
            case 'R':
                facing = (facing + 1) % 4
            case 'L':
                facing = (facing - 1) % 4
            case amount_str:
                amount = int(amount_str)
                for _ in range(amount):
                    i, j = pos
                    di, dj = directions[facing]
                    i, j = i + di, j + dj

                    new_pos = i, j
                    new_facing = facing
                    
                    if new_pos not in tiles:
                        match facing:
                            case 0:
                                if 0 < i <= 50:
                                    new_pos = 151 - i, 100
                                    new_facing = 2
                                elif 50 < i <= 100:
                                    new_pos = 50, 50 + i
                                    new_facing = 3
                                elif 100 < i <= 150:
                                    new_pos = 51 - (i - 100), 150
                                    new_facing = 2
                                else:
                                    new_pos = 150, 50 + (i - 150)
                                    new_facing = 3
                            case 1:
                                if 100 < j <= 150:
                                    new_pos = 50 + (j - 100), 100
                                    new_facing = 2
                                elif 50 < j <= 100:
                                    new_pos = 150 + (j - 50), 50
                                    new_facing = 2
                                else:
                                    new_pos = i - 200, j + 100
                                    new_facing = facing
                            case 2:
                                if 0 < i <= 50:
                                    new_pos = 151 - i, 1
                                    new_facing = 0
                                elif 50 < i <= 100:
                                    new_pos = 101, i - 50
                                    new_facing = 1
                                elif 100 < i <= 150:
                                    new_pos = 151 - i, 51
                                    new_facing = 0
                                else:
                                    new_pos = 1, 50 + (i - 150)
                                    new_facing = 1
                            case 3:
                                if 0 < j <= 50:
                                    new_pos = 50 + j, 51
                                    new_facing = 0
                                elif 50 < j <= 100:
                                    new_pos = 100 + j, 1
                                    new_facing = 0
                                else:
                                    new_pos = 200, j - 100
                                    new_facing = facing
                                
                    if tiles[new_pos] == '.':
                        pos = new_pos
                        facing = new_facing
                    else:
                        break

    i, j = pos
    yield 1000 * (i + 1) + 4 * (j + 1) + facing


run(solve, skip_sample=True, parts=(2,))
