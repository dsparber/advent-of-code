

def count_ones(lines, index):
    count = 0
    for line in lines:
        char = line[index]
        if char == "1":
            count += 1
    return count


with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    total = len(lines)
    bits = len(lines[0])

    oxygen_lines = [line for line in lines]
    for index in range(bits):
        count = count_ones(oxygen_lines, index)
        filter_bit = "1" if count >= len(oxygen_lines) / 2 else "0"
        oxygen_lines = [line for line in oxygen_lines if line[index] == filter_bit]
        if len(oxygen_lines) == 1:
            break

    co2_lines = [line for line in lines]
    for index in range(bits):
        count = count_ones(co2_lines, index)
        filter_bit = "0" if count >= len(co2_lines) / 2 else "1"
        co2_lines = [line for line in co2_lines if line[index] == filter_bit]
        if len(co2_lines) == 1:
            break

    oxygen_bits = oxygen_lines[0]
    co2_bits = co2_lines[0]

    oxygen_decimal = int(oxygen_bits, 2)
    co2_decimal = int(co2_bits, 2)

    print("oxygen = {} ({}), co2 = {} ({})".format(oxygen_bits, oxygen_decimal, co2_bits, co2_decimal))
    print("product = {}".format(oxygen_decimal * co2_decimal))
