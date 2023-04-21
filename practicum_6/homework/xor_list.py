from __future__ import annotations
from dataclasses import dataclass
from typing import Any

import ctypes
import yaml


@dataclass
class Element:
    key: Any
    data: Any = None
    np: int = 0

    def next(self) -> Element:
        return self.np ^ prev_p
    def prev(self) -> Element:
        return self.np ^ next_p

class XorDoublyLinkedList:
    def __init__(self) -> None:
        self.head: Element = None
        self.tail: Element = None
        self.nodes: list[Element] = []


    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return " <-> ".join(str(current.key) for current in iter(self))
        
    def get(self, p_id: int) -> Element:
        return ctypes.cast(p_id, ctypes.py_object).value
        
    def to_pylist(self) -> list[Any]:
        py_list = []
        next_id = id(self.head)
        prev_id = 0

        while next_id != 0:
            next_el = ctypes.cast(next_id, ctypes.py_object).value
            py_list.append(next_el.key)
            prev_id, next_id = next_id, next_el.next(prev_id)

        return py_list

    def empty(self):
        return self.head is None

    def search(self, k: Element) -> Element:
        """Complexity: O(n)"""
        if self.empty():
            raise ValueError("List empty")
        node = self.head
        while node and node.key != k.key:
            node = node.next(id(node))
        if not node:
            raise ValueError("List havnt got this element")
        return node

    def insert(self, x: Element) -> None:
        """Insert to the front of the list (i.e., it is 'prepend')
        Complexity: O(1)
        """
        if self.head is None:
            self.head = self.tail = x
        else:
            x.np = id(self.head)
            self.head.np ^= id(x)
            self.head, x = x, self.head
        self.nodes.insert(0, x)
    def _get_element(self, p_id: int) -> Element:
        return ctypes.cast(p_id, ctypes.py_object).value

    def remove(self, x: Element) -> None:
        """Remove x from the list
        Complexity: O(1)
        """
        curr_id,prev_id,curr_el = id(self.head),0,self.head
        
        while curr_id and curr_el.key != x.key:
            prev_id, curr_id = curr_id, curr_el.next(prev_id)
            curr_el = self.get(curr_id)
        if curr_id:
            next_id = curr_el.next(prev_id)
            if next_id:
                next_el = self.get(next_id)
                next_el.np = next_el.np ^ curr_id ^ prev_id
            else:
                self.tail = prev_el
            if prev_id:
                prev_el = self.get(prev_id)
                prev_el.np = prev_el.np ^ curr_id ^ next_id
            else:
                self.head = next_id
                prev_el = None
            self.nodes.remove(curr_el)
        else:
            raise ValueError("Element not found in the list.")

    def reverse(self) -> XorDoublyLinkedList:
        """Returns the same list but in the reserved order
        Complexity: O(1)
        """
        if not self:
            raise ValueError("List is empty!")
    
        self.head, self.tail = self.tail, self.head
        return self


if __name__ == "__main__":
    # You need to implement a doubly linked list using only one pointer
    # self.np per element. In python, by pointer, we understand id(object).
    # Any object can be accessed via its id, e.g.
    # >>> import ctypes
    # >>> a = ...
    # >>> ctypes.cast(id(a), ctypes.py_object).value
    # Hint: assuming that self.next and self.prev store pointers
    # define self.np as self.np = self.next XOR self.prev

    with open("practicum_6/homework/xor_list_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        l = XorDoublyLinkedList()
        for el in reversed(c["input"]["list"]):
            l.insert(Element(key=el))
        for op_info in c["input"]["ops"]:
            if op_info["op"] == "insert":
                l.insert(Element(key=op_info["key"]))
            elif op_info["op"] == "remove":
                l.remove(Element(key=op_info["key"]))
            elif op_info["op"] == "reverse":
                l = l.reverse()
        py_list = l.to_pylist()
        print(f"Case #{i + 1}: {py_list == c['output']}")
