from dataclasses import dataclass, field
from typing import Tuple


@dataclass
class Node:
    data: int
    parent: 'Node' = field(repr=False)
    left: 'Node' = field(repr=False)
    right: 'Node' = field(repr=False)


class SplayTreeUtils:
    _pinf = float('inf')

    def search(root: Node, data: int) -> Tuple[Node, bool]:
        prev, curr = None, root
        while curr is not None:
            if data == curr.data:
                return SplayTreeUtils._splay(curr), True
            if data < curr.data:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        return SplayTreeUtils._splay(prev), False

    def insert(root: Node, data: int) -> Node:
        node = Node(data, None, None, None)
        curr = root
        while curr is not None:
            if data < curr.data:
                if curr.left is None:
                    node.parent = curr
                    curr.left = node
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    node.parent = curr
                    curr.right = node
                    break
                curr = curr.right
        return SplayTreeUtils._splay(node)

    def delete(root: Node, data: int) -> Tuple[Node, bool]:
        nroot, found = SplayTreeUtils.search(root, data)
        if not found:
            return nroot, found
        
        lnode = nroot.left
        rnode = nroot.right
        nroot.left = nroot.right = None
        if lnode is not None:
            lnode.parent = None
        if rnode is not None:
            rnode.parent = None
        return SplayTreeUtils._join(lnode, rnode), True

    def _join(lroot: Node, rroot: Node) -> Node:
        if rroot is None:
            return lroot
        if lroot is None:
            return rroot
        lroot, _ = SplayTreeUtils.search(lroot, SplayTreeUtils._pinf)
        lroot.right = rroot
        rroot.parent = lroot
        return lroot

    def _splay(node: Node) -> Node:
        while node is not None and node.parent is not None:
            pnode = node.parent
            gnode = pnode.parent
            if gnode is not None:
                if gnode.left is pnode:
                    if pnode.left is node:
                        SplayTreeUtils._zig(gnode)
                        SplayTreeUtils._zig(pnode)
                    else:
                        SplayTreeUtils._zag(pnode)
                        SplayTreeUtils._zig(gnode)
                else:
                    if pnode.left is node:
                        SplayTreeUtils._zig(pnode)
                        SplayTreeUtils._zag(gnode)
                    else:
                        SplayTreeUtils._zag(gnode)
                        SplayTreeUtils._zag(pnode)
            else:
                if pnode.left is node:
                    SplayTreeUtils._zig(pnode)
                else:
                    SplayTreeUtils._zag(pnode)
        return node
        
    def _zig(node: Node) -> Node:
        lnode = node.left
        if node.parent is not None:
            if node.parent.left is node:
                node.parent.left = lnode
            else:
                node.parent.right = lnode
        node.left = lnode.right
        if node.left is not None:
            node.left.parent = node
        lnode.right = node
        lnode.parent = node.parent
        node.parent = lnode
        return lnode
    
    def _zag(node: Node) -> Node:
        rnode = node.right
        if node.parent is not None:
            if node.parent.left is node:
                node.parent.left = rnode
            else:
                node.parent.right = rnode
        node.right  = rnode.left
        if node.right is not None:
            node.right.parent = node
        rnode.left = node
        rnode.parent = node.parent
        node.parent = rnode
        return rnode

snode = None
snode = SplayTreeUtils.insert(snode, 3)
snode = SplayTreeUtils.insert(snode, 34)
snode = SplayTreeUtils.insert(snode, 2)
snode = SplayTreeUtils.insert(snode, -9)
snode = SplayTreeUtils.insert(snode, 89)
