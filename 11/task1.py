def neighbors(row, col):
    return [(row + dy, col + dx)
            for dx, dy
            in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            if 0 <= row + dy < rows and 0 <= col + dx < cols]


def flash(row, col):
    energy, flashed = states[row][col]
    if energy <= 9 or flashed:
        return

    states[row][col] = 0, True
    for n_row, n_col in neighbors(row, col):
        n_energy, n_flashed = states[n_row][n_col]
        if not n_flashed:
            states[n_row][n_col] = n_energy + 1, False
            flash(n_row, n_col)


def print_state():
    for row in range(rows):
        print("".join([str(n) for n, _ in states[row]]))


with open("input", "r") as f:
    states = [[(int(char), False) for char in line.strip()] for line in f.readlines()]
    rows, cols = len(states), len(states[0])

    flashes = 0
    for _ in range(100):
        states = [[(n + 1, False) for n, _ in row] for row in states]
        for row in range(rows):
            for col in range(cols):
                flash(row, col)
        flashes += sum([sum([1 if flashed else 0 for _, flashed in row]) for row in states])

    print(flashes)
