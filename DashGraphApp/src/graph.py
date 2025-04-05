from pathlib import Path
from typing import Set
import networkx as nx
import itertools as it

import dash

# path_graph = Path(__file__).parent.parent / "database" / "g.95.2.graphml"
# path_graph = Path(__file__).parent.parent / "database" / "newyork.graphml"
# graph: nx.DiGraph = nx.read_graphml(path_graph)

ls_nodes = []
path_graph = Path(__file__).parent.parent / "database" / "Wiki-Vote.txt"
with open(path_graph, "r") as fo:
    for line in fo:
        if line.startswith("#"):
            continue
        line = line.strip().split("\t")
        if len(line) != 2:
            continue
        ls_nodes += [line]
graph = nx.DiGraph(ls_nodes)
for n, data in graph.nodes(True):
    data["layer"] = 0


def get_descendants(root: str | None) -> Set[str]:
    if not root:
        return []
    return nx.descendants(graph, root)

def get_ascendants(leaf: str | None) -> Set[str]:
    if not leaf:
        return []
    return nx.ancestors(graph, leaf)


def get_subgraph(root: str | None = None, leaf: str | None = None) -> nx.DiGraph:
    ret = graph
    if root:
        if root:
            ret = nx.subgraph(graph, get_descendants(root) | {root})
        if leaf:
            ret = nx.subgraph(ret, get_ascendants(leaf) | {leaf})
    return ret
    
    
def simplify_graph(graph: nx.DiGraph, root: str | None) -> nx.DiGraph:
    ret = nx.DiGraph()
    if root:
        for n, path in nx.single_source_shortest_path(graph, root).items():
            data = graph.nodes[n]
            data["layer"] = len(path)
            ret.add_node(n, **data)
            for e_in, e_out in it.pairwise(path):
                ret.add_edge(e_in, e_out)
    return ret
