from itertools import combinations
from typing import Iterable, Optional

from sympy import solve, var, Eq

from utils import run


def solve_day_24(input_data: str) -> Iterable[int]:
    trajectories = [
        [tuple(map(int, coordinates.split(", "))) for coordinates in line.split(" @ ")]
        for line in input_data.splitlines()
    ]

    yield num_intersections(trajectories)
    yield find_ray_for_rock(trajectories)


def num_intersections(trajectories: list[...]) -> int:
    is_sample = len(trajectories) == 5
    lower, upper = (7, 27) if is_sample else (200000000000000, 400000000000000)

    count = 0
    for a, b in combinations(trajectories, 2):
        intersection = compute_intersection(a, b)

        if intersection is not None:
            x, y = intersection
            if lower <= x <= upper and lower <= y <= upper:
                count += 1
    return count


def compute_intersection(a: tuple[tuple], b: tuple[tuple]) -> Optional[tuple[int, ...]]:
    (ax, ay, _), (adx, ady, _) = a
    (bx, by, _), (bdx, bdy, _) = b

    if ady / adx == bdy / bdx:
        return None  # Parallel lines

    x = 1 / (ady / adx - bdy / bdx) * (ady / adx * ax - bdy / bdx * bx + by - ay)
    y = ady / adx * x + (ay - ady / adx * ax)

    if (x - ax) / adx < 0 or (x - bx) / bdx < 0:
        return None  # Crossed in the past

    return x, y


def find_ray_for_rock(trajectories: list[...]) -> int:
    px, py, pz = var("px"), var("py"), var("pz")
    vx, vy, vz = var("vx"), var("vy"), var("vz")

    eq = []

    for i, ((pix, piy, piz), (vix, viy, viz)) in enumerate(trajectories[:3]):
        ti = var(f"t{i}")

        eq.append(Eq(px + vx * ti, pix + vix * ti))
        eq.append(Eq(py + vy * ti, piy + viy * ti))
        eq.append(Eq(pz + vz * ti, piz + viz * ti))

    ans = solve(eq)[0]

    return int(ans[px] + ans[py] + ans[pz])


run(solve_day_24)
