with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    grid = [[int(char) for char in line] for line in lines]

    rows = len(grid)
    cols = len(grid[0])

    risk_sum = 0

    for row in range(rows):
        for col in range(cols):
            is_low_point = True
            for neighbor_row, neighbor_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    if grid[neighbor_row][neighbor_col] <= grid[row][col]:
                        is_low_point = False
            if is_low_point:
                risk_level = grid[row][col] + 1
                risk_sum += risk_level

    print(risk_sum)
