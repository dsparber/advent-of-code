with open('input') as f:
    grid = [[char for char in line.strip()] for line in f.readlines()]
    rows, cols = len(grid), len(grid[0])

    count = 0
    while True:
        moved = False

        for direction in [">", "v"]:
            new_grid = [['.' for _ in row] for row in grid]
            for i0 in range(rows):
                for j0 in range(cols):

                    i1, j1 = (i0 + 1) % rows if direction == 'v' else i0, \
                             (j0 + 1) % cols if direction == '>' else j0

                    if grid[i0][j0] == direction and grid[i1][j1] == '.':
                        moved = True
                        new_grid[i1][j1] = grid[i0][j0]

                    elif grid[i0][j0] != '.':
                        new_grid[i0][j0] = grid[i0][j0]

            grid = new_grid

        count += 1
        if not moved:
            break

    print(f"Part 1: {count}")
