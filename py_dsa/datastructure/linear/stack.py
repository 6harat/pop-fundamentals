from dataclasses import dataclass, field


@dataclass
class Node:
    data: int
    next: 'Node' = field(repr=False)


class Stack:

    def __init__(self):
        self._head: Node = None

    def peek(self) -> int:
        if self._head is None:
            return None
        return self._head.data

    def pop(self) -> int:
        if self._head is None:
            return None
        node = self._head
        self._head = node.next
        return node.data

    def push(self, data: int) -> None:
        node = Node(data, self._head)
        self._head = node

    def is_empty(self) -> bool:
        return self._head is None
