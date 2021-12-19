from itertools import product, permutations

alignments = [(permutation, signs) for permutation in permutations(range(3)) for signs in product([-1, 1], repeat=3)]


def transform(coordinates, alignment):
    (i, j, k), (si, sj, sk) = alignment
    for coordinate in coordinates:
        yield coordinate[i] * si, coordinate[j] * sj, coordinate[k] * sk


def coord_diff(a, b):
    return tuple(map(lambda a_i, b_i: b_i - a_i, a, b))


def find_alignment(reference, other):
    for alignment in alignments:
        other_transformed = list(transform(other, alignment))
        possible_deltas = {coord_diff(a, b) for a in reference for b in other_transformed}
        for delta in possible_deltas:
            shifted = [coord_diff(delta, coord) for coord in other_transformed]
            if sum([1 if (x, y, z) in reference else 0 for x, y, z in shifted]) >= 12:
                return shifted, delta

    return None, None


with open('input') as f:
    scanners = [[tuple(map(int, r.split(','))) for r in d.split('\n')[1:]] for d in ''.join(f.readlines()).split('\n\n')]
    unmatched = set(range(1, len(scanners)))
    checked_pairs = set()
    deltas = set()

    while unmatched:
        matched = set(range(len(scanners))).difference(unmatched)
        to_check = set(product(matched, unmatched)).difference(checked_pairs)
        for i, j in to_check:
            aligned_beacons, delta = find_alignment(scanners[i], scanners[j])
            checked_pairs.add((i, j))
            if aligned_beacons:
                unmatched.remove(j)
                scanners[j] = aligned_beacons
                deltas.add(delta)
                break

    # Task 1
    print(len({coord for scanner in scanners for coord in scanner}))

    # Task 2
    print(max(sum(map(abs, coord_diff(a, b))) for a, b in product(deltas, repeat=2)))
