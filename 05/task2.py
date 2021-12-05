
def parse_line(line):
    split = line.split(" -> ")
    coord_1 = split[0].split(",")
    coord_2 = split[1].split(",")
    return (int(coord_1[0]), int(coord_1[1])), (int(coord_2[0]), int(coord_2[1]))


with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    vents = [parse_line(line) for line in lines]

    covered = dict()

    for (x1, y1), (x2, y2) in vents:
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)

        if x_min == x_max:
            x = x_min
            for y in range(y_min, y_max + 1):
                covered[(x, y)] = covered.get((x, y), 0) + 1
        elif y1 == y2:
            y = y_min
            for x in range(x_min, x_max + 1):
                covered[(x, y)] = covered.get((x, y), 0) + 1
        elif (x_max - x_min) == (y_max - y_min):
            x_dir = 1 if x2 > x1 else -1
            y_dir = 1 if y2 > y1 else -1
            # print("{} -> {}".format((x1, y1), (x2, y2)))
            for delta in range(0, (x_max - x_min) + 1):
                x, y = (x1 + delta * x_dir), (y1 + delta * y_dir)
                # print((x, y))
                covered[(x, y)] = covered.get((x, y), 0) + 1
        else:
            print("Should not happen")

    values_at_least_2 = len(list(filter(lambda count: count >= 2, covered.values())))
    print(values_at_least_2)


