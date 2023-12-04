from functools import cache
from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    cards = [
        [
            [
                int(number.strip())
                for number in numbers_str.replace("  ", " ").strip().split(" ")
            ]
            for numbers_str in line.split(":")[1].split("|")
        ]
        for line in (input_data.split("\n"))
    ]
    cards_with_id = list(enumerate(cards))
    cards_by_id = dict(cards_with_id)
    card_ids = list(cards_by_id.keys())

    @cache
    def count_matches(card_id: int) -> int:
        winning_numbers, my_numbers = cards_by_id[card_id]
        return len([number for number in my_numbers if number in winning_numbers])

    def points(card_id: int) -> int:
        return int(2 ** (count_matches(card_id) - 1))

    yield sum(map(points, card_ids))

    num_processed_cards = 0
    unprocessed_cards = card_ids

    while unprocessed_cards:
        num_processed_cards += 1
        card_id = unprocessed_cards.pop()
        for i in range(count_matches(card_id)):
            copy_id = card_id + 1 + i
            unprocessed_cards.append(copy_id)

    yield num_processed_cards


run(solve)
