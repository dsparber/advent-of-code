with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    corresponding = {o: c for o, c in zip(opening, closing)}

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    score = 0
    for line in lines:
        stack = []
        for char in line:
            if char in opening:
                stack.append(char)
            else:
                expected = corresponding[stack.pop()]
                if expected != char:
                    score += points[char]
                    break

    print(score)
