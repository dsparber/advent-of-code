
with open("input", "r") as f:
    numbers = [int(v) for v in f.readlines()]

    count = 0
    for i in range(1, len(numbers) - 2):
        if sum(numbers[i:(i+3)]) > sum(numbers[(i-1):(i+2)]):
            count += 1

    print(count)
