
with open("input", "r") as f:
    aim = 0
    depth, horizontal = 0, 0

    for line in f.readlines():
        match line.split():
            case ["down", value]: aim += int(value)
            case ["up", value]: aim -= int(value)
            case ["forward", value]:
                horizontal += int(value)
                depth += aim * int(value)

    print("depth = {}, horizontal = {}, product = {}".format(depth, horizontal, depth * horizontal))
