from collections import defaultdict, Counter
from itertools import product

with open('input') as f:
    positions = tuple([int(line.split()[-1]) for line in f.readlines()])

    states = defaultdict(int)
    states[(positions, (0, 0))] = 1

    win_counts = [0, 0]
    dice_possibilities = Counter([sum(throws) for throws in product((1, 2, 3), repeat=3)])

    player = 0
    while states:
        new_states = defaultdict(int)
        for (positions, score), count in states.items():
            for dice_sum, possibilities in dice_possibilities.items():
                new_positions, new_score = list(positions), list(score)
                new_positions[player] = (positions[player] + dice_sum - 1) % 10 + 1
                new_score[player] += new_positions[player]
                if new_score[player] >= 21:
                    win_counts[player] += count * possibilities
                else:
                    new_states[(tuple(new_positions), tuple(new_score))] += count * possibilities

        states = new_states
        player = (player + 1) % 2

    print(max(win_counts))
