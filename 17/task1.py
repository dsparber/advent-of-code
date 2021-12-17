with open('input') as f:
    x_string, y_string = f.readlines()[0].replace("target area: x=", "").replace(", y=", " ").split()
    x_min, x_max = map(int, x_string.split(".."))
    y_min, y_max = map(int, y_string.split(".."))

    print(x_min, x_max, y_min, y_max)

    max_value = 0

    for vx0 in range(x_max):
        for vy0 in range(-y_min):
            vx, vy = vx0, vy0
            px, py = 0, 0
            trajectory = []
            while True:
                px, py = px + vx, py + vy
                vx, vy = vx - 1 if vx > 0 else 0, vy - 1
                trajectory.append((px, py))
                if x_min <= px <= x_max and y_min <= py <= y_max:
                    max_value = max(max_value, max([y for _, y in trajectory]))
                    break
                if py < y_min:
                    break

    print(max_value)



