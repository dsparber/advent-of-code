from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    x = 1
    cycle = 0
    signal_strengths = [0]
    image = ""
    for line in input_data.split('\n'):
        duration, delta = 1, 0
        match line.split(' '):
            case ["addx", v]: duration, delta = 2, int(v)

        for _ in range(duration):
            image += "#" if x - 1 <= cycle % 40 <= x + 1 else '.'
            cycle += 1
            signal_strengths.append(cycle * x)
            if cycle % 40 == 0:
                image += "\n"

        x += delta

    yield sum([signal_strengths[i] for i in range(20, len(signal_strengths), 40)])
    print(image)


run(solve)
