def deterministic_dice():
    while True:
        for i in range(1, 101):
            yield i


with open('input') as f:
    positions = [int(line.split()[-1]) for line in f.readlines()]
    scores = [0, 0]

    dice = deterministic_dice()
    roll_count = 0

    player = 0
    while max(scores) < 1000:
        dice_value = next(dice) + next(dice) + next(dice)
        roll_count += 3
        positions[player] = (positions[player] + dice_value - 1) % 10 + 1
        scores[player] += positions[player]
        player = (player + 1) % 2

    print(roll_count * min(scores))
