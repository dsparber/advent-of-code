
with open("input", "r") as f:
    lines = f.readlines()
    numbers = [int(v) for v in lines]

    count = -1
    last_sum = -1
    for i in range(len(numbers) - 2):
        sliding_sum = 0
        for j in range(3):
            sliding_sum += numbers[i + j]

        print(sliding_sum)

        if sliding_sum > last_sum:
            count += 1

        last_sum = sliding_sum

    print("Result: {}".format(count))
