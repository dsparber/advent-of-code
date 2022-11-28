from collections import defaultdict, Counter

with open("input", "r") as f:

    G = defaultdict(list)
    for u, v in [line.strip().split("-") for line in f.readlines()]:
        G[u].append(v)
        G[v].append(u)

    paths = [['start']]
    total_paths = 0

    while paths:
        new_paths = []
        for path in paths:
            u = path[-1]
            if u == 'end':
                total_paths += 1
                continue

            path_counts = Counter(path)
            has_small_twice = len([v for v, count in path_counts.items() if v.islower() and count == 2]) > 0
            for v in G[u]:
                if v.isupper() or v not in path or (path_counts[v] == 1 and not has_small_twice and v != 'start'):
                    new_paths.append(path + [v])

        paths = new_paths

    print(total_paths)
