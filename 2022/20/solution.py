from collections import deque
from typing import Iterable

from utils import run


def decrypt(numbers: list[int], n: int) -> int:
    positions = list(enumerate(numbers))
    mixed = deque(positions.copy())
    for _ in range(n):
        for p in positions:
            idx = mixed.index(p)
            mixed.rotate(-idx)
            pos, value = mixed.popleft()
            mixed.rotate(-value)
            mixed.appendleft((pos, value))

    mixed_list = [value for _, value in mixed]
    zero_idx = mixed_list.index(0)
    return sum([mixed_list[(zero_idx + i) % len(positions)] for i in [1000, 2000, 3000]])


def solve(input_data: str) -> Iterable[int]:
    numbers = [int(v) for v in input_data.splitlines()]
    yield decrypt(numbers, 1)
    decrypted_numbers = [v * 811589153 for v in numbers]
    yield decrypt(decrypted_numbers, 10)


run(solve)
