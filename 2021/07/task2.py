def fuel_cost(a, b):
    diff = abs(a - b)
    return diff * (diff + 1) // 2

with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    positions = [int(x) for x in lines[0].split(",")]

    min_pos = min(positions)
    max_pos = max(positions)

    min_fuel = len(positions) * (max_pos - min_pos + 1)**2  # An upper bound
    for p in range(min_pos, max_pos + 1):
        min_fuel = min(min_fuel, sum([fuel_cost(pos, p) for pos in positions]))

    print(min_fuel)
