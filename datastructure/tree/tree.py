from dataclasses import dataclass
from collections import deque


@dataclass
class Node:
    data: int
    left: 'Node'
    right: 'Node'


class TreeUtils:
    def preorder(root: Node):
        if root is None:
            return
        print(root.data, end=",")
        TreeUtils.preorder(root.left)
        TreeUtils.preorder(root.right)
    
    def preorder_iter(root: Node):
        curr = root
        stack = []
        while curr or stack:
            if curr is None:
                curr = stack.pop().right
            else:
                print(curr.data, end=",")
                stack.append(curr)
                curr = curr.left
    
    def inorder(root: Node):
        if root is None:
            return
        TreeUtils.inorder(root.left)
        print(root.data, end=",")
        TreeUtils.inorder(root.right)
    
    def inorder_iter(root: Node):
        curr = root
        stack = []
        while curr or stack:
            if curr is None:
                curr = stack.pop()
                print(curr.data, end=",")
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left
    
    def postorder(root: Node):
        if root is None:
            return
        TreeUtils.postorder(root.left)
        TreeUtils.postorder(root.right)
        print(root.data, end=",")
    
    def postorder_iter(root: Node):
        curr = root
        stack = []
        opstack = []
        while curr or stack:
            if curr is None:
                curr = stack.pop().left
            else:
                opstack.append(curr.data)
                stack.append(curr)
                curr = curr.right
        print(",".join(map(str, reversed(opstack))))

    def levelorder(root: Node):
        pass

    def levelorder_iter(root: Node):
        dq = deque([root])
        while dq:
            el = dq.popleft()
            if el is None:
                continue
            print(el.data, end=",")
            dq.append(el.left)
            dq.append(el.right)
    
    def levelorder_iter_newline(root: Node):
        cutoff = object()
        dq = deque([root, cutoff])
        while dq:
            el = dq.popleft()
            if el == cutoff:
                print()
                if dq:
                    dq.append(cutoff)
                continue
            if el is None:
                continue
            print(el.data, end=",")
            dq.append(el.left)
            dq.append(el.right)
    
    def reverse_levelorder_iter(root: Node):
        dq = deque([root])
        stack = []
        while dq:
            el = dq.popleft()
            if el is None:
                continue
            stack.append(el.data)
            dq.append(el.right)
            dq.append(el.left)
        print(",".join(map(str, reversed(stack))))

    def spiralorder_iter(root: Node):
        dstack = [root]
        bstack = []
        flag = True
        while dstack or bstack:
            if flag:
                while dstack:
                    el = dstack.pop()
                    if el is None:
                        continue
                    print(el.data, end=",")
                    bstack.append(el.left)
                    bstack.append(el.right)
                flag = not flag
            else:
                while bstack:
                    cl = bstack.pop()
                    if cl is None:
                        continue
                    print(cl.data, end=",")
                    dstack.append(cl.right)
                    dstack.append(cl.left)
                flag = not flag

    def checksum(root: Node, hash: int) -> bool:
        if root is None:
            return False
        
        delta = hash-root.data
        if root.left is None and root.right is None:
            return delta == 0
        
        return TreeUtils.checksum(root.left, delta) or TreeUtils.checksum(root.right, delta)

    def lca(root: Node, a: int, b: int) -> int:
        pass
