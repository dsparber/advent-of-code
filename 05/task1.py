
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
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                point = (x1, y)
                covered[point] = covered.get(point, 0) + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                point = (x, y1)
                covered[point] = covered.get(point, 0) + 1

    values_at_least_2 = len(list(filter(lambda count: count >= 2, covered.values())))
    print(values_at_least_2)


