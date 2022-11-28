
with open("input", "r") as f:
    depth, horizontal = 0, 0

    for line in f.readlines():
        match line.split():
            case ["forward", value]: horizontal += int(value)
            case ["down", value]: depth += int(value)
            case ["up", value]: depth -= int(value)

    print("depth = {}, horizontal = {}, product = {}".format(depth, horizontal, depth * horizontal))
