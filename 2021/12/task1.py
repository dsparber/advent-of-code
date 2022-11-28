from collections import defaultdict

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

            for v in G[u]:
                if v.isupper() or v not in path:
                    new_paths.append(path + [v])

        paths = new_paths

    print(total_paths)
