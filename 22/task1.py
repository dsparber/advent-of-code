import re


def parse(line):
    command = line.split()[0]
    numbers = tuple(map(int, re.findall(r"-?\d+", line)))
    return command, (numbers[:2], numbers[2:4], numbers[4:])


def intersecting_range(a, b):
    (a0, a1), (b0, b1) = a, b
    start, end = max(a0, b0), min(a1, b1)
    return range(start, end + 1)


with open('input') as f:
    steps = [parse(line) for line in f.readlines()]

    on = set()
    for command, (x_range, y_range, z_range) in steps:
        for x in intersecting_range(x_range, (-50, 50)):
            for y in intersecting_range(y_range, (-50, 50)):
                for z in intersecting_range(z_range, (-50, 50)):
                    if command == 'on':
                        on.add((x, y, z))
                    elif (x, y, z) in on:
                        on.remove((x, y, z))

    print(len(on))
