from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    return total_score(input_data, 0), total_score(input_data, 1)


def total_score(input_data: str, smudges) -> int:
    total = 0
    for pattern in input_data.split("\n\n"):
        rows = pattern.splitlines()
        cols = ["".join([row[j] for row in rows]) for j in range(len(rows[0]))]
        total += symmetry_score(cols, smudges) + 100 * symmetry_score(rows, smudges)

    return total


def symmetry_score(lines: list[str], smudges: int = 0) -> int:
    num_lines = len(lines)

    for i, row in enumerate(lines[:-1]):
        difference = 0

        for k in range(num_lines):
            row_a, row_b = i - k, i + k + 1
            if 0 <= row_a < row_b < num_lines:
                difference += sum(
                    [1 for a, b in zip(lines[row_a], lines[row_b]) if a != b]
                )

        if difference == smudges:
            return i + 1

    return 0


run(solve)
