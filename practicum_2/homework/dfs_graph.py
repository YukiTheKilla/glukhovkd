import queue
from typing import Any

import networkx as nx

from src.plotting import plot_graph


def visit(node: Any):
    print(f"Wow, it is {node} right here!")


def dfs_iterative(G: nx.Graph, node: Any) -> None:
    visited = {n: False for n in G}
    
    q = queue.LifoQueue()
    q.put(node)
    
    while not q.empty():
        point = q.get()
        if visited[point]:
            continue
        visit(point)
        visited[point] = 1
        
        nonvisited = list(filter(lambda neighbor: \
        not visited[neighbor], G.neighbors(point)))
        for neighbor in nonvisited:
            q.put(neighbor)


def topological_sort(G: nx.DiGraph, node: Any):
    visited = {n: False for n in G}
    
    q = queue.LifoQueue()
    q.put(node)
    
    while not q.empty():
        point = q.get()
        if visited[point]:
            continue
        visit(point)
        visited[point] = 1
        
        unvisited = list(filter(lambda ancestors: \
        not visited[ancestors], \
        nx.ancestors(G,point)))
        if len(unvisited) <= 0:
            for successors in G.successors(point):
                q.put(successors)


if __name__ == "__main__":
    # Load and plot the graph
    G = nx.read_edgelist("practicum_2/homework/graph_2.edgelist", create_using=nx.Graph)
    # plot_graph(G)

    print("Iterative DFS")
    print("-" * 32)
    dfs_iterative(G, node="0")
    print()

    G = nx.read_edgelist(
        "practicum_2/homework/graph_2.edgelist", create_using=nx.DiGraph
    )
    plot_graph(G)
    print("Topological sort")
    print("-" * 32)
    topological_sort(G, node="0")
