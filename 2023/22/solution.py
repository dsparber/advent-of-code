from dataclasses import dataclass, field
from typing import Iterable

from portion import closed

from utils import run


def solve(input_data: str) -> Iterable[int]:
    bricks = sorted(
        list(map(Brick.parse, enumerate(input_data.splitlines()))),
        key=lambda b: b.z_min,
    )

    settled_bricks = []
    for brick in bricks:
        candidates = [b for b in settled_bricks if b.intersects_horizontally(brick)]
        support_z = max([c.z_max for c in candidates], default=0)
        supporting_bricks = [c for c in candidates if c.z_max == support_z]
        brick.move_to_z(support_z + 1)
        brick.supported_by = supporting_bricks
        for supporter in supporting_bricks:
            supporter.supports.append(brick)
        settled_bricks.append(brick)

    yield sum(map(Brick.can_be_disintegrated, bricks))
    yield sum(map(Brick.number_of_falling_bricks, bricks))


@dataclass
class Brick:
    number: int
    start: tuple[int, int, int]
    end: tuple[int, int, int]
    supports: list["Brick"] = field(default_factory=list)
    supported_by: list["Brick"] = field(default_factory=list)

    def move_to_z(self, z: int) -> None:
        x0, y0, z0 = self.start
        x1, y1, z1 = self.end
        dz = z0 - z
        self.start = x0, y0, z0 - dz
        self.end = x1, y1, z1 - dz

    def intersects_horizontally(self, other: "Brick") -> bool:
        a_x0, a_y0, _ = self.start
        a_x1, a_y1, _ = self.end

        b_x0, b_y0, _ = other.start
        b_x1, b_y1, _ = other.end

        return not (
            closed(a_x0, a_x1).intersection(closed(b_x0, b_x1)).empty
            or closed(a_y0, a_y1).intersection(closed(b_y0, b_y1)).empty
        )

    def can_be_disintegrated(self) -> bool:
        for supports_brick in self.supports:
            if len(supports_brick.supported_by) <= 1:
                return False
        return True

    def number_of_falling_bricks(self) -> int:
        if self.can_be_disintegrated():
            return 0

        disintegrated = {self.number}
        queue = [] + self.supports
        while queue:
            current = queue.pop()
            any_support_remaining = False
            for supporter in current.supported_by:
                if supporter.number not in disintegrated:
                    any_support_remaining = True

            if not any_support_remaining:
                disintegrated.add(current.number)
                queue += current.supports

        return len(disintegrated - {self.number})

    @property
    def z_min(self) -> int:
        return self.start[2]

    @property
    def z_max(self) -> int:
        return self.end[2]

    @staticmethod
    def parse(item: tuple[int, str]) -> "Brick":
        number, line = item
        start, end = (tuple(map(int, part.split(","))) for part in line.split("~"))
        return Brick(number, start, end)


run(solve)
