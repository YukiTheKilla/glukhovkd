from typing import Any

import networkx as nx

from src.plotting import plot_graph
import numpy as np
import queue

def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    shortest_paths = {}  # key = destination node, value = list of intermediate nodes
    shortest_paths[source_node] = [source_node]
    
    visited = set()
    distance = {neighbor: np.inf for neighbor in G.nodes}
    if distance == source_node:
        return 0
    
    q = queue.PriorityQueue()
    q.put((0, source_node))
    
    while not q.empty():
        length, node = q.get()
        if node not in visited:
            visited.add(node)
            
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                current_length = length + G.edges[neighbor, node]["weight"]
            if current_length < distance[neighbor]:
                shortest_paths[neighbor] = [neighbor] + shortest_paths[node]
                distance[neighbor] = current_length
                q.put((distance[neighbor], neighbor))

    return shortest_paths


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    shortest_paths = dijkstra_sp(G, source_node="0")
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
