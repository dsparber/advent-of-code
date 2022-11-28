import math


def neighbors(vertex):
    row, col = vertex
    return [(row + dy, col + dx)
            for dx, dy
            in [(-1, 0),  (0, -1), (0, 1), (1, 0)]
            if 0 <= row + dy < rows and 0 <= col + dx < cols]


with open("input", "r") as f:
    numbers = [[int(char) for char in line.strip()] for line in f.readlines()]
    rows, cols = len(numbers), len(numbers[0])

    vertices = {(row, col) for row in range(rows) for col in range(cols)}

    d = {v: math.inf for v in vertices}

    Q = {(0, 0)}
    d[(0, 0)] = 0

    while Q:
        u = min(Q, key=lambda v: d[v])
        Q.remove(u)

        for v in neighbors(u):
            new_d = d[u] + numbers[v[0]][v[1]]
            if new_d < d[v]:
                d[v] = new_d
                Q.add(v)

    print(d[(rows-1, cols-1)])

