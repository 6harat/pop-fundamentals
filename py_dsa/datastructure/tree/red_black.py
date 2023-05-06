from dataclasses import dataclass, field
from enum import Enum
from turtle import color

# https://www.youtube.com/watch?v=UaLIHuR1t8Q&list=PLrmLmBdmIlpv_jNDXtJGYTPNQ2L1gdHxu&index=25
# black root
# no red-red
# black nodes along all leaves > 2 same

# if empty tree => black node
# create red node
#    if parent black: done
#    else:
#        if no/black sibling => rotate and recolor
#        if red sibling => recolor (sibling=> black, parent=>red only if it is not root) => check again

class Color(Enum):
    BLACK = 0
    RED = 1

@dataclass
class Node:
    data: int
    color: Color
    left: 'Node' = field(repr=False)
    right: 'Node' = field(repr=False)


class RedBlackTreeUtils:
    def search(root: Node, data: int) -> bool:
        pass

    def _balance(root: Node) -> None:
        if root.left is not None and root.left.color == Color.RED:
            if root.left.left is not None and root.left.left.color == Color.RED:
                if root.right is None or root.right.color == Color.BLACK:
                    nroot = root.left
                    root.left = nroot.right
                    nroot.right = root
                    nroot.color = Color.BLACK
                    root.color = Color.RED
                    return nroot
                else:
                    root.color = Color.RED
                    root.left = Color.BLACK
                    root.right = Color.BLACK
                    return root
            elif root.left.right is not None and root.left.right.color == Color.RED:
                if root.right is None or root.right.color == Color.BLACK:
                    nroot = root.left.right
                    root.left.right = nroot.left
                    nroot.left = root.left
                    root.left = nroot.right
                    nroot.right = root
                    nroot.color = Color.BLACK
                    root.color = Color.RED
                    return nroot
                else:
                    root.color = Color.RED
                    root.left = Color.BLACK
                    root.right = Color.BLACK
                    return root
        if root.right is not None and root.right.color == Color.RED:
            if root.right.right is not None and root.right.right.color == Color.RED:
                if root.left is None or root.left.color == Color.BLACK:
                    nroot = root.right
                    root.right = nroot.left
                    nroot.left = root
                    nroot.color = Color.BLACK
                    root.color = Color.RED
                    return nroot
                else:
                    root.color = Color.RED
                    root.left = Color.BLACK
                    root.right = Color.BLACK
                    return root
            elif root.right.left is not None and root.right.left.color == Color.RED:
                if root.left is None or root.left.color == Color.BLACK:
                    nroot = root.right.left
                    root.right.left = nroot.right
                    nroot.right = root.right
                    root.right = nroot.left
                    nroot.left = root
                    nroot.color = Color.BLACK
                    root.color = Color.RED
                    return nroot
                else:
                    root.color = Color.RED
                    root.left = Color.BLACK
                    root.right = Color.BLACK
                    return root
        return root

    def _insert(root: Node, data: int) -> Node:
        if root is None:
            return Node(data, Color.BLACK, None, None)
        
        if data < root.data:
            if root.left is None:
                root.left = Node(data, Color.RED, None, None)
            else:
                RedBlackTreeUtils._insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data, Color.RED, None, None)
            else:
                RedBlackTreeUtils._insert(root.right, data)

        RedBlackTreeUtils._balance(root)
        return root
    
    def insert(root: Node, data: int) -> Node:
        root = RedBlackTreeUtils._insert(root, data)
        root.color = Color.BLACK
        return root

    # def insert_iter(root: Node, data: int) -> Node:
    #     if root is None:
    #         return Node(data, Color.BLACK, None, None)
        
    #     stack = [root]
    #     node = Node(data, Color.RED, None, None)
    #     while node is not None:
    #         el = stack[-1]
    #         if data < el.data:
    #             if el.left is None:
    #                 el.left = node
    #                 stack.append(node)
    #                 node = None
    #             else:
    #                 stack.append(el.left)
    #         else:
    #             if el.right is None:
    #                 el.right = node
    #                 stack.append(node)
    #                 node = None
    #             else:
    #                 stack.append(el.right)

    #     child = stack.pop()
    #     while stack:
    #         parent = stack[-1]
    #         if parent.color == Color.BLACK:
    #             return root
            
    #     return root


# left-leaning-red-black-tree
# ref: https://www.geeksforgeeks.org/left-leaning-red-black-tree-insertion/

t = None
t = RedBlackTreeUtils.insert(t, 10)
t = RedBlackTreeUtils.insert(t, 20)
t = RedBlackTreeUtils.insert(t, -10)
t = RedBlackTreeUtils.insert(t, 15)
