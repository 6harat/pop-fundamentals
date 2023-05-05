from dataclasses import dataclass, field
from typing import Callable

# height-biased
# weight-biased

@dataclass
class Node:
    data: int
    npl: int
    left: 'Node' = field(repr=False)
    right: 'Node' = field(repr=False)


@dataclass
class LeftistHeap:
    cmp: Callable[[int, int], int]

    def __post_init__(self) -> None:
        self._head :Node = None

    def push(self, data: int) -> None:
        node = Node(data, 1, None, None)
        self._head = self._merge(self._head, node)

    def pop(self) -> int:
        if self._head is None:
            return None
        node = self._head
        self._head = self._merge(node.left, node.right)
        return node.data

    def peek(self) -> int:
        if self._head is None:
            return None
        return self._head.data

    def decrease_key(self):
        raise NotImplementedError

    def delete_key(self):
        raise NotImplementedError

    def _merge(self, ahead: Node, bhead: Node) -> Node:
        if bhead is None:
            return ahead
        if ahead is None:
            return bhead
        if self.cmp(ahead.data, bhead.data) <= 0:
            phead = ahead
            chead = bhead
        else:
            phead = bhead
            chead = ahead

        phead.right = self._merge(phead.right, chead)
        lnpl = 0 if phead.left is None else phead.left.npl
        rnpl = 0 if phead.right is None else phead.right.npl
        if rnpl > lnpl:
            tmp = phead.left
            phead.left = phead.right
            phead.right = tmp
        phead.npl = min(lnpl, rnpl) + 1
        return phead


min_cmp = lambda a, b: 0 if a==b else -1 if a < b else 1
max_cmp = lambda a, b: 0 if a==b else -1 if a > b else 1

lhmin = LeftistHeap(min_cmp)
nums = [5, -1, 3, 5, 7, 8, 9, 4, 2]
for n in nums:
    lhmin.push(n)
