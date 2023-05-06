from collections import deque
from dataclasses import dataclass, field
import random
from typing import Callable, Deque, Tuple


@dataclass
class Node:
    data: int
    priority: int
    left: 'Node' = field(repr=False)
    right: 'Node' = field(repr=False)


@dataclass
class Treap:
    priority_cmp: Callable[[int, int], int]
    priority_range: Tuple[int, int]

    def __post_init__(self):
        self._root: Node = None
        self._random = random.Random(23)
        self._generate_priority = lambda: self._random.randint(*self.
                                                               priority_range)

    def search(self, data: int) -> bool:
        curr = self._root
        while curr is not None:
            if data == curr.data:
                return True

            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def insert(self, data: int) -> None:
        curr = self._root
        node = Node(data, self._generate_priority(), None, None)
        stack: Deque[Node] = deque()
        while curr is not None:
            stack.append(curr)
            if data < curr.data:
                if curr.left is None:
                    curr.left = node
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                    break
                curr = curr.right
        stack.append(node)
        cnode = stack.pop()
        while stack and self.priority_cmp(cnode.priority,
                                          stack[-1].priority) < 0:
            pnode = stack.pop()
            if cnode.data < pnode.data:
                pnode.left = cnode.right
                cnode.right = pnode
                if stack:
                    if stack[-1].left is pnode:
                        stack[-1].left = cnode
                    else:
                        stack[-1].right = cnode
            else:
                pnode.right = cnode.left
                cnode.left = pnode
                if stack:
                    if stack[-1].left is pnode:
                        stack[-1].left = cnode
                    else:
                        stack[-1].right = cnode
        if not stack:
            self._root = cnode
        return

    def delete(root: Node, data: int) -> Node:
        # find the key using BST search
        # mark its priority as worst
        # rotate down till it becomes a leaf node
        # delete
        pass

    def pop(root: Node) -> Node:
        pass

    def _join(root: Node) -> Node:
        pass


min_cmp = lambda a, b: 0 if a == b else -1 if a < b else 1
max_cmp = lambda a, b: 0 if a == b else -1 if a > b else 1
tr = Treap(min_cmp, (0, 100))
nums = [5, -1, 3, 5, 7, 8, 9, 4, 2]
for n in nums:
    tr.insert(n)
