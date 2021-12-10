with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    corresponding = {o: c for o, c in zip(opening, closing)}

    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    scores = []
    for line in lines:
        discard = False
        stack = []
        for char in line:
            if char in opening:
                stack.append(char)
            else:
                expected = corresponding[stack.pop()]
                if expected != char:
                    discard = True
                    break

        if not discard:
            completion_score = 0
            while stack:
                missing = corresponding[stack.pop()]
                completion_score = completion_score * 5 + points[missing]

            scores.append(completion_score)

    scores.sort()
    print(scores[len(scores)//2])
