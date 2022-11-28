from itertools import product

with open('input') as f:
    lines = [line.strip() for line in f.readlines()]

    code = [''.join(['1' if char == '#' else '0' for char in row]) for row in lines[0]]
    image = [['1' if char == '#' else '0' for char in row] for row in lines[2:]]
    inf_pixel = '0'

    for _ in range(50):
        rows = len(image)
        cols = len(image[0])
        output = []
        for i in range(-1, rows + 1):
            output_row = []
            output.append(output_row)
            for j in range(-1, cols + 1):
                cells = [(i + di, j + dj) for di, dj in product((-1, 0, 1), repeat=2)]
                bitstring = ''.join([image[r][c] if 0 <= r < rows and 0 <= c < cols else inf_pixel for r, c in cells])
                output_row.append(code[int(bitstring, base=2)])

        image = output
        inf_pixel = code[int(inf_pixel * 9, base=2)]

    print(sum([sum(map(int, row)) for row in image]))
