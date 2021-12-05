
with open("input", "r") as f:
    lines = f.readlines()

    aim = 0
    depth, horizontal = 0, 0
    for line in lines:
        command, value_str = line.split(" ")
        value = int(value_str)

        if command == "down":
            aim += value
        if command == "up":
            aim -= value
        if command == "forward":
            horizontal += value
            depth += aim * value

    print("depth = {}, horizontal = {}".format(depth, horizontal))
    print("product = {}".format(depth * horizontal))
