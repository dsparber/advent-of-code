from itertools import cycle

from utils import run


def solve_for_steps(input_data: str, steps) -> int:
    jet_pattern = [-1 if direction == '<' else 1 for direction in input_data]
    rock_types = [[[v == '#' for v in row] for row in rock.split('\n')][::-1] for rock in
                        ["####", ".#.\n###\n.#.", "..#\n..#\n###", "#\n#\n#\n#", "##\n##"]]

    chamber = list()

    jet_index = 0
    rock_index = 0
    cache = dict()

    for step in range(steps):
        height = len(chamber)

        key = rock_index, jet_index
        if key not in cache:
            cache[key] = step, height
        else:
            old_step, old_height = cache[key]
            repeat_length = step - old_step
            remaining_steps = steps - step

            if remaining_steps % repeat_length == 0:
                return height + remaining_steps // repeat_length * (height - old_height)

        rock = rock_types[rock_index]
        rock_index = (rock_index + 1) % len(rock_types)

        rock_width = len(rock[0])
        x, y = 2, len(chamber) + 3

        def is_valid(x, y):
            if x < 0 or x + rock_width > 7:
                return False

            for rock_line, chamber_line in zip(rock, chamber[y:]):
                for rock_solid, blocked in zip(rock_line, chamber_line[x:]):
                    if rock_solid and blocked:
                        return False
            return True

        while True:
            jet = jet_pattern[jet_index]
            jet_index = (jet_index + 1) % len(jet_pattern)

            # Pushed by jet
            if is_valid(x + jet, y):
                x += jet

            # Fall down
            if y > 0 and is_valid(x, y - 1):
                y -= 1
            else:
                break

        # Update chamber
        for i, rock_line in enumerate(rock, y):
            if len(chamber) <= i:
                chamber.append([False] * 7)
            for j, solid in enumerate(rock_line):
                chamber[i][x + j] = chamber[i][x + j] or solid

    return len(chamber)

def solve(input_data: str) -> tuple[int, int]:
    return solve_for_steps(input_data, 2022), solve_for_steps(input_data, 1_000_000_000_000)


run(solve)
