from dataclasses import dataclass, field


@dataclass
class Node:
    data: int
    left: 'Node' = field(repr=False)
    right: 'Node' = field(repr=False)


class BstUtils:
    def equals(rootA: Node, rootB: Node) -> bool:
        if rootA is None and rootB is None:
            return True
        
        if rootA is None or rootB is None:
            return False
        
        return rootA.data == rootB.data and BstUtils.equals(
            rootA.left, rootB.left) and BstUtils.equals(
                rootA.right, rootB.right)
    
    def search(root: Node, data: int) -> bool:
        while root:
            if data == root.data:
                return True
            if data < root.data:
                root = root.left
            else:
                root = root.right
        return False

    def insert(root: Node, data: int) -> Node:
        n = Node(data, None, None)
        if root is None:
            return n
        
        tmp = root
        while True:
            if data < tmp.data:
                if tmp.left is None:
                    tmp.left = n
                    return root
                tmp = tmp.left
            else:
                if tmp.right is None:
                    tmp.right = n
                    return root
                tmp = tmp.right

    def lca(root: Node, a: int, b: int) -> int:
        if root is None:
            return root
        if root.data > max(a, b):
            return BstUtils.lca(root.left, a, b)
        elif root.data < min(a, b):
            return BstUtils.lca(root.right, a, b)
        else:
            return root.data

    def _next_node(root: Node, val: int) -> Node:
        if root is None:
            return root
        if val < root.data:
            return root.left
        return root.right

    def lca_iter(root: Node, a: int, b: int) -> int:
        while root:
            if root.data == a or root.data == b:
                return root.data
            anode = BstUtils._next_node(root, a)
            bnode = BstUtils._next_node(root, b)
            if anode != bnode:
                return root.data
            root = anode
        return None
