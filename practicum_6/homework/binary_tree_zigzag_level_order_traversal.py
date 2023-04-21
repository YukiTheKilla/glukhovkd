from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from collections import deque

import yaml


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None
    right: Node = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def zigzag_level_order_traversal(self) -> list[Any]:
        if not self.root:
            return []
    
        levels, q, reverse = [], deque([self.root]), False
    
        while q:
            level = [q.popleft() for _ in range(len(q))]
            if reverse:
                level = level[::-1]
            levels.append([node.key for node in level])
            q += [child for node in level for child in (node.left, node.right) if child]
            reverse = not reverse
    
        return levels


def build_tree(list_view: list[Any]) -> BinaryTree:
    bt = BinaryTree()
    nodes = [Node(val) if val is not None else None for val in list_view]
    if nodes:
        children = nodes[::-1]
        bt.root = children.pop()
        for node in nodes:
            if node:
                node.left = children.pop() if children else None
                node.right = children.pop() if children else None
    return bt


if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open(
        "practicum_6/homework/binary_tree_zigzag_level_order_traversal_cases.yaml", "r"
    ) as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = build_tree(c["input"])
        zz_traversal = bt.zigzag_level_order_traversal()
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
