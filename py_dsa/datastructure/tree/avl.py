from dataclasses import dataclass, field


@dataclass
class Node:
    data: int
    left: 'Node' = field(repr=False)
    right: 'Node' = field(repr=False)
    height: int


class AvlUtils:
    def _left_left_rotate(root: Node) -> Node:
        nroot = root.left
        root.left = nroot.right
        nroot.right = root

        nroot.right.height = AvlUtils.height(nroot.right)
        nroot.height = AvlUtils.height(nroot)
        return nroot

    def _left_right_rotate(root: Node) -> Node:
        nroot = root.left.right
        root.left.right = nroot.left
        nroot.left = root.left
        root.left = nroot.right
        nroot.right = root
        
        nroot.left.height = AvlUtils.height(nroot.left)
        nroot.right.height = AvlUtils.height(nroot.right)
        nroot.height = AvlUtils.height(nroot)
        return nroot

    def _right_right_rotate(root: Node) -> Node:
        nroot = root.right
        root.right = nroot.left
        nroot.left = root

        nroot.left.height = AvlUtils.height(nroot.left)
        nroot.height = AvlUtils.height(nroot)
        return nroot

    def _right_left_rotate(root: Node) -> Node:
        nroot = root.right.left
        root.right.left = nroot.right
        nroot.right = root.right
        root.right = nroot.left
        nroot.left = root
        
        nroot.left.height = AvlUtils.height(nroot.left)
        nroot.right.height = AvlUtils.height(nroot.right)
        nroot.height = AvlUtils.height(nroot)
        return nroot

    def height(root: Node) -> Node:
        if root == None:
            return 0
        lheight = 0 if root.left is None else root.left.height
        rheight = 0 if root.right is None else root.right.height
        return 1+max(lheight, rheight)

    def _balance(root: Node) -> Node:
        lheight = AvlUtils.height(root.left)
        rheight = AvlUtils.height(root.right)
        if abs(lheight-rheight) < 2:
            return root
        
        if lheight > rheight:
            llheight = AvlUtils.height(root.left.left)
            lrheight = AvlUtils.height(root.left.right)
            if llheight > lrheight:
                return AvlUtils._left_left_rotate(root)
            else:
                return AvlUtils._left_right_rotate(root)
        else:
            rrheight = AvlUtils.height(root.right.right)
            rlheight = AvlUtils.height(root.right.left)
            if rrheight > rlheight:
                return AvlUtils._right_right_rotate(root)
            else:
                return AvlUtils._right_left_rotate(root)

    def insert(root: Node, data: int) -> Node:
        n = Node(data, None, None, 1)
        if root is None:
            return n
        
        if data < root.data:
            root.left = AvlUtils.insert(root.left, data)
        else:
            root.right = AvlUtils.insert(root.right, data)

        root.height = AvlUtils.height(root)
        return AvlUtils._balance(root)

avl1 = None
for data in [1, 2, 3, 6, 5, -2, -5, -8]:
    avl1 = AvlUtils.insert(avl1, data)
