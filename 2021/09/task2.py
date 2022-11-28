def neighbors(row, col):
    return [(r, c)
            for r, c
            in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            if 0 <= r < rows and 0 <= c < cols]


with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    grid = [[int(char) for char in line] for line in lines]

    rows = len(grid)
    cols = len(grid[0])

    low_points = []

    for row in range(rows):
        for col in range(cols):
            is_low_point = True
            for neighbor_row, neighbor_col in neighbors(row, col):
                if grid[neighbor_row][neighbor_col] <= grid[row][col]:
                    is_low_point = False
            if is_low_point:
                low_points.append((row, col))

    basin_sizes = list()
    visited = [[False] * cols for row in range(rows)]

    for low_point in low_points:
        # Use DFS to find size of basin
        size = 0
        stack = [low_point]
        while stack:
            row, col = stack.pop()
            if not visited[row][col]:
                visited[row][col] = True
                size += 1
                for n_row, n_col in neighbors(row, col):
                    if grid[n_row][n_col] < 9:
                        stack.append((n_row, n_col))

        basin_sizes.append(size)

    basin_sizes.sort(reverse=True)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])