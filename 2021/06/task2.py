from collections import defaultdict

with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    ages_count = defaultdict(int)  # Group by age
    for age in lines[0].split(","):
        ages_count[int(age)] += 1

    for _ in range(256):
        new_ages_count = defaultdict(int)
        for age, num_fish in ages_count.items():
            if age == 0:
                new_ages_count[6] += num_fish
                new_ages_count[8] += num_fish
            else:
                new_ages_count[age - 1] += num_fish
        ages_count = new_ages_count

    print(sum(ages_count.values()))
