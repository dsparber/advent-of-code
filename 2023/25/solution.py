from typing import Iterable

from math import prod
from networkx import Graph, connected_components, minimum_edge_cut

from utils import run


def solve(input_data: str) -> Iterable[int]:
    graph = Graph()

    for line in input_data.splitlines():
        vertex, neighbors = line.split(": ")
        for neighbor in neighbors.split(" "):
            graph.add_edge(vertex, neighbor)

    min_cut = minimum_edge_cut(graph)
    graph.remove_edges_from(min_cut)

    yield prod(map(len, connected_components(graph)))


run(solve)
