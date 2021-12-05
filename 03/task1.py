
with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    total = len(lines)
    bits = len(lines[0])
    counts = [0] * bits
    for line in lines:
        for index, char in enumerate(line):
            if char == "1":
                counts[index] += 1

    gamma = ""
    epsilon = ""

    for count in counts:
        if count > total / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)

    print("gamma = {} ({}), epsilon = {} ({})".format(gamma, gamma_decimal, epsilon, epsilon_decimal))
    print("product = {}".format(gamma_decimal * epsilon_decimal))
