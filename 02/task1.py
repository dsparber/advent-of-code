
with open("input", "r") as f:
    lines = f.readlines()

    depth, horizontal = 0, 0
    for line in lines:
        command, value_str = line.split(" ")
        value = int(value_str)

        if command == "forward":
            horizontal += value
        if command == "down":
            depth += value
        if command == "up":
            depth -= value

    print("depth = {}, horizontal = {}".format(depth, horizontal))
    print("product = {}".format(depth * horizontal))
