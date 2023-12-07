from collections import Counter
from functools import partial
from typing import Iterable

from utils import run


def solve(input_data: str) -> Iterable[int]:
    hands_with_bids = [
        (line.split(" ")[0], int(line.split(" ")[1]))
        for line in input_data.splitlines()
    ]

    def type_strength(hand: str, use_jokers: bool) -> int:
        num_jokers = 0
        if use_jokers:
            num_jokers = hand.count("J")
            hand = hand.replace("J", "")

        hand_counts = sorted(Counter(hand).values(), reverse=True)
        most_common_card_count = num_jokers + (hand_counts[0] if hand_counts else 0)

        return [
            most_common_card_count == 5,  # Five of a kind
            most_common_card_count == 4,  # Four of a kind
            # Full house
            [3, 2] == hand_counts[:2]
            or ([2, 2] == hand_counts[:2] and num_jokers == 1),
            most_common_card_count == 3,  # Three of a kind
            [2, 2] == hand_counts[:2],  # Two pairs
            most_common_card_count == 2,  # One Pair
            True,  # High card
        ].index(True)

    def strength(hand_and_bid: tuple[str, int], use_jokers: bool) -> tuple:
        hand, _ = hand_and_bid
        card_ranks = "J23456789TQKA" if use_jokers else "23456789TJQKA"
        return type_strength(hand, use_jokers), list(map(card_ranks[::-1].index, hand))

    def winnings(use_jokers: bool) -> int:
        sorted_hands = sorted(
            hands_with_bids, key=partial(strength, use_jokers=use_jokers), reverse=True
        )
        return sum([rank * bid for rank, (_, bid) in enumerate(sorted_hands, 1)])

    return winnings(use_jokers=False), winnings(use_jokers=True)


run(solve)
