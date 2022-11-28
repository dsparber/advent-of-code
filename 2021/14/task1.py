from collections import defaultdict

with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    letter_counts = defaultdict(int)
    for letter in lines[0]:
        letter_counts[letter] += 1

    pairs = defaultdict(int)
    for pair in [lines[0][i:(i+2)] for i in range(len(lines[0]) - 1)]:
        pairs[pair] += 1

    replacements = {k: v for k, v in [line.split(" -> ") for line in lines[2:]]}

    for _ in range(10):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            if pair in replacements.keys():
                letter = replacements[pair]
                p1, p2 = pair[0] + letter, letter + pair[1]
                new_pairs[p1] += count
                new_pairs[p2] += count
                letter_counts[letter] += count
        pairs = new_pairs

    print(max(letter_counts.values()) - min(letter_counts.values()))

