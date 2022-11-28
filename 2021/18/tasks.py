import itertools
import functools


def depth(number):
    match number:
        case [a, b]: return 1 + max(depth(a), depth(b))
        case _: return 0


def add_left(number, value):
    match number:
        case [a, b]: return [add_left(a, value), b]
        case x: return x + value


def add_right(number, value):
    match number:
        case [a, b]: return [a, add_right(b, value)]
        case x: return x + value


def explode(number, current_depth=0):
    match number:
        case [a, b] if current_depth == 4: return a, 0, b
        case [a, b] if current_depth + depth(a) == 4:
            left, a, right = explode(a, current_depth + 1)
            return left, [a, add_left(b, right) if right else b], None
        case [a, b] if current_depth + depth(b) == 4:
            left, b, right = explode(b, current_depth + 1)
            return None, [add_right(a, left) if left else a, b], right
        case x: return None, x, None


def needs_split(number):
    match number:
        case [a, b]: return needs_split(a) or needs_split(b)
        case x: return x >= 10


def split(number):
    match number:
        case [a, b] if needs_split(a): return [split(a), b]
        case [a, b] if needs_split(b): return [a, split(b)]
        case x if x >= 10: return [x // 2, (x + 1) // 2]
        case x: return x


def reduce(number):
    if depth(number) == 5: return reduce(explode(number)[1])
    if needs_split(number): return reduce(split(number))
    return number


def add(a, b):
    return reduce([a, b])


def magnitude(number):
    match number:
        case [a, b]: return 3 * magnitude(a) + 2 * magnitude(b)
        case x: return x


with open('input') as f:
    numbers = [eval(line.strip()) for line in f.readlines()]

    print(magnitude(functools.reduce(add, numbers)))
    print(max([magnitude(add(a, b)) for a, b in itertools.permutations(numbers, 2)]))
