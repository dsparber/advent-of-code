with open("input", "r") as f:
    paper = set()
    folds = []

    for line in f.readlines():
        if "," in line:
            x, y = line.split(",")
            paper.add((int(x), int(y)))
        if "fold" in line:
            axis, number = line.split()[2].split("=")
            folds.append((axis, int(number)))

    axis, number = folds[0]
    match axis:
        case 'x': paper = {(x, y) if x < number else (2 * number - x, y) for x, y in paper}
        case 'y': paper = {(x, y) if y < number else (x, 2 * number - y) for x, y in paper}

    print(len(paper))
