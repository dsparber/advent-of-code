
index = dict(w=0, x=1, y=2, z=3)


def apply_arithmetic(state, line_number):
    while line_number < len(lines) and not lines[line_number].startswith('inp'):
        operator, a, b = lines[line_number].split()
        idx = index[a]
        result = state[idx]
        value = state[index[b]] if b in index.keys() else int(b)
        match operator:
            case 'add': result += value
            case 'mul': result *= value
            case 'div': result //= value
            case 'mod': result %= value
            case 'eql': result = 1 if result == value else 0

        state = state[:idx] + (result, ) + state[idx+1:]
        line_number += 1

    return state, line_number


def compute_next(current, find_largest):
    state, line_number, number = current

    _, a = lines[line_number].split()
    idx = index[a]
    for i in range(1, 10) if find_largest else reversed(range(1, 10)):
        new_state = state[:idx] + (i, ) + state[idx+1:]

        result_state, result_line_number = apply_arithmetic(new_state, line_number + 1)
        yield result_state, result_line_number, number * 10 + i


def dfs(find_largest, ignored_prefixes):
    s = [((0, 0, 0, 0), 0, 0)]

    visited = set()

    while s:
        state, line_number, input_number = s.pop()

        if input_number in ignored_prefixes:
            continue  # This is kind of a heck, but

        if line_number == len(lines):
            if state[index['z']] == 0:
                return input_number
            else:
                continue

        lookup = line_number, state[index['z']]
        if lookup in visited:
            continue
        visited.add(lookup)

        for result in compute_next((state, line_number, input_number), find_largest):
            s.append(result)


with open('input') as f:
    lines = f.readlines()
    # ignored_prefixes: skip numbers that start with these prefixes
    # Be aware, that the ignored_prefixes depend on the given input!
    # For my personal input it turned out that the largest accepted
    # number starts with a 2 and the smallest starts with 14.
    print(f"\rPart 1: {dfs(find_largest=True, ignored_prefixes=[9, 8, 7, 6, 5, 4, 3])}")
    print(f"\rPart 2: {dfs(find_largest=False, ignored_prefixes=[11, 12, 13])}")
