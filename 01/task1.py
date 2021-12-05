
with open("input", "r") as f:
    numbers = [int(v) for v in f.readlines()]

    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            count += 1

    print(count)
