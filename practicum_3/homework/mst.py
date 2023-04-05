import queue
from typing import Any

import matplotlib.pyplot as plt
import networkx as nx

from src.plotting import plot_graph

def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()  # set of nodes included into MST
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    mst_edges = set()  # set of edges constituting MST

    mst_set.add(start_node)
    rest_set.remove(start_node)

    q = queue.PriorityQueue()
    
    while len(rest_set)>0: 
        for node_neighbor in G.neighbors(start_node):
            if (node_neighbor in mst_set):
                continue
            new_edge = (start_node,node_neighbor)
            q.put((G.edges[new_edge]["weight"],new_edge))

        new_edge = q.get()
        if new_edge[1][1] in mst_set:
            continue

        start_node = new_edge[1][1]
        mst_set.add(start_node)
        rest_set.remove(start_node)
        mst_edges.add(new_edge[1])

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
