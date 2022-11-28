with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    ages = [int(x) for x in lines[0].split(",")]

    for _ in range(80):
        num_ages = len(ages)
        for i in range(num_ages):
            if ages[i] == 0:
                ages[i] = 6
                ages.append(8)
            else:
                ages[i] -= 1

    print(len(ages))
