from dataclasses import dataclass, field
import math
from typing import Callable


@dataclass
class Node:
    data: int
    degree: int
    mark: bool
    parent: 'Node' = field(repr=False)
    psibling: 'Node' = field(repr=False)
    nsibling: 'Node' = field(repr=False)
    child: 'Node' = field(repr=False)


@dataclass
class FibonacciHeap:
    cmp: Callable[[int, int], int]

    def __post_init__(self) -> None:
        self._head :Node = None
        self._n :int = 0

    def push(self, data: int) -> None:
        node = Node(data, 0, False, None, None, None, None)
        node.psibling = node
        node.nsibling = node
        self._head = self._union_heaps(node, self._head)
        self._n += 1

    def pop(self) -> int:
        node = self._head
        if node is None:
            return None

        self._head = self._purge_node(node)
        self._dettach_parent(node.child)
        self._n -= 1
        self._head = self._union_heaps(node.child, self._head)
        self._head = self._concatenate(self._head)
        node.child = None
        return node.data

    def peek(self) -> int:
        if self._head is None:
            return None
        return self._head.data

    def decrease_key(self):
        raise NotImplementedError

    def delete_key(self):
        raise NotImplementedError

    def _union_heaps(self, ahead, bhead) -> Node:
        if ahead is None:
            return bhead
        if bhead is None:
            return ahead
        bprev = bhead.psibling
        anext = ahead.nsibling

        bhead.psibling = ahead
        ahead.nsibling = bhead

        anext.psibling = bprev
        bprev.nsibling = anext

        if self.cmp(ahead.data, bhead.data) < 0:
            return ahead
        return bhead
    
    def _purge_node(self, node: Node) -> Node:
        if node.psibling is node:
            return None

        prev = node.psibling
        prev.nsibling = node.nsibling
        node.nsibling.psibling = prev
        node.psibling = node.nsibling = node
        return prev.nsibling

    def _concatenate(self, head: Node) -> Node:
        if head is None:
            return None
        
        mdegree = self._max_degree()
        buffer = [None]*(mdegree+1)
        curr = head
        while buffer[curr.degree] != curr:
            if buffer[curr.degree] is None:
                buffer[curr.degree] = curr
                curr = curr.nsibling
            else:
                node = buffer[curr.degree]
                buffer[curr.degree] = None
                self._purge_node(node)
                next = self._purge_node(curr)
                curr = self._merge_nodes(node, curr)
                self._union_heaps(curr, next)
        mhead, ohead = curr, curr
        curr = curr.nsibling
        while curr != ohead:
            if self.cmp(curr.data, mhead.data) < 0:
                mhead = curr
            curr = curr.nsibling
        return mhead
        
    def _max_degree(self) -> int:
        return int(math.log2(self._n))+1

    def _merge_nodes(self, anode: Node, bnode: Node) -> Node:
        if self.cmp(anode.data, bnode.data) <= 0:
            self._attach_child(anode, bnode)
            return anode
        self._attach_child(bnode, anode)
        return bnode

    def _attach_child(self, pnode: Node, cnode: Node) -> None:
        pnode.degree += 1
        cnode.parent = pnode
        pnode.child = self._union_heaps(cnode, pnode.child)

    def _dettach_parent(self, node: Node) -> None:
        if node is None:
            return
        node.parent = None
        curr = node.nsibling
        while curr != node:
            curr.parent = None
            curr = curr.nsibling


min_cmp = lambda a, b: 0 if a==b else -1 if a < b else 1
max_cmp = lambda a, b: 0 if a==b else -1 if a > b else 1

fhmin = FibonacciHeap(min_cmp)
nums = [5, -1, 3, 5, 7, 8, 9, 4, 2]
for n in nums:
    fhmin.push(n)
