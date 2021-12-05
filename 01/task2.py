
with open("input", "r") as f:
    numbers = [int(v) for v in f.readlines()]

    count = 0
    for i in range(1, len(numbers) - 2):
        if numbers[i+2] > numbers[i-1]:
            count += 1

    print(count)
