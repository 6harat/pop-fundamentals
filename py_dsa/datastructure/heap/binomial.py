from dataclasses import dataclass
from typing import Callable, Tuple


@dataclass
class Node:
    data: int
    degree: int
    parent: 'Node'
    lchild: 'Node'
    sibling: 'Node'


@dataclass
class BinomialHeap:
    cmp: Callable[[int, int], int]

    def __post_init__(self) -> None:
        self._head: Node = None

    def push(self, data: int):
        node = Node(data, 0, None, None, None)
        self._head = self._union_heaps(self._head, node)

    def pop(self) -> int:
        prev, node = self._find_min()
        if node is None:
            return None

        if prev is None:
            self._head = node.sibling
        else:
            prev.sibling = node.sibling

        self._dettach_parent(node.lchild)
        self._head = self._union_heaps(node.lchild, self._head)
        node.lchild = node.sibling = None
        return node.data

    def peek(self) -> int:
        _, node = self._find_min()
        return None if node is None else node.data

    def decrease_key(self):
        raise NotImplementedError

    def delete_key(self):
        raise NotImplementedError

    def _find_min(self) -> Tuple[Node, Node]:
        if self._head is None:
            return None, None
        mprev, mnode, prev, node = None, self._head, self._head, self._head.sibling
        while node is not None:
            if self.cmp(mnode.data, node.data) > 0:
                mprev = prev
                mnode = node
            prev = node
            node = node.sibling
        return mprev, mnode

    def _union_heaps(self, ahead: Node, bhead: Node) -> Node:
        if ahead is None:
            return bhead
        if bhead is None:
            return ahead

        if ahead.degree <= bhead.degree:
            mhead = mcurr = ahead
            ahead = ahead.sibling
        else:
            mhead = mcurr = bhead
            bhead = bhead.sibling

        while ahead is not None and bhead is not None:
            if ahead.degree <= bhead.degree:
                mcurr.sibling = ahead
                ahead = ahead.sibling
            else:
                mcurr.sibling = bhead
                bhead = bhead.sibling
            mcurr = mcurr.sibling

        if ahead is None:
            mcurr.sibling = bhead
        else:
            mcurr.sibling = ahead

        return self._concatentate(mhead)

    def _concatentate(self, head: Node) -> Node:
        ohead = head
        prev, curr, next = None, head, head.sibling
        while curr is not None and next is not None:
            if curr.degree == next.degree and (
                    next.sibling is None or next.sibling.degree > curr.degree):
                curr = self._merge_nodes(curr)
                if prev is None:
                    ohead = curr
                else:
                    prev.sibling = curr
                next = curr.sibling
            else:
                prev = curr
                curr = next
                next = curr.sibling
        return ohead

    def _merge_nodes(self, node: Node) -> Node:
        if self.cmp(node.data, node.sibling.data) <= 0:
            cnode = node.sibling
            node.sibling = cnode.sibling
            cnode.sibling = None
            self._attach_child(node, cnode)
            return node
        else:
            pnode = node.sibling
            node.sibling = None
            self._attach_child(pnode, node)
            return pnode

    def _attach_child(self, pnode: Node, cnode: Node) -> None:
        pnode.degree += 1
        cnode.parent = pnode
        if pnode.lchild is None:
            pnode.lchild = cnode
        else:
            snode = pnode.lchild
            # TODO: always attach as left child to make push O(1) and reverse during union operation
            while snode.sibling is not None:
                snode = snode.sibling
            snode.sibling = cnode

    def _dettach_parent(self, node: Node) -> None:
        while node is not None:
            node.parent = None
            node = node.sibling


min_cmp = lambda a, b: 0 if a == b else -1 if a < b else 1
max_cmp = lambda a, b: 0 if a == b else -1 if a > b else 1

bhmin = BinomialHeap(min_cmp)
nums = [5, -1, 3, 5, 7, 8, 9, 4, 2]
for n in nums:
    bhmin.push(n)
