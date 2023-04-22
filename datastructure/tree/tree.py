from dataclasses import dataclass, field
from collections import deque
from typing import List, Tuple


@dataclass
class Node:
    data: int
    left: 'Node' = field(repr=False)
    right: 'Node' = field(repr=False)


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

    def postorder_iter1(root: Node):
        curr = root
        stack = []
        while curr or stack:
            if curr is None:
                curr = stack.pop()
                print(curr.data, end=",")
                if stack:
                    if curr == stack[-1].right or not stack[-1].right:
                        curr = None
                    else:
                        curr = stack[-1].right
                else:
                    curr = None
            else:
                stack.append(curr)
                curr = curr.left or curr.right or None

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

    def search(root: Node, a: int) -> bool:
        curr = root
        stack = []
        while curr or stack:
            if curr is None:
                curr = stack.pop().right
            else:
                if curr.data == a:
                    return True
                stack.append(curr)
                curr = curr.left
        return False

    def findpath(root: Node, a: int) -> List[int]:
        stack = [(root, 0)]
        while stack:
            el = stack[-1]
            if el[0] is None:
                stack.pop()
                continue
            if el[1] == 2:
                stack.pop()
            elif el[1] == 1:
                stack[-1] = (el[0], 2)
                stack.append((el[0].right, 0))
            else:
                if el[0].data == a:
                    return [k[0] for k in stack]
                stack[-1] = (el[0], 1)
                stack.append((el[0].left, 0))
        return None

    def lca(root: Node, a: int, b: int) -> int:
        if root is None:
            return None
        lval = TreeUtils.lca(root.left, a, b)
        rval = TreeUtils.lca(root.right, a, b)
        if lval is None and rval is None:
            return root.data if root.data == a or root.data == b else None
        if lval is None:
            return root.data if (root.data == a and rval == b) or (
                root.data == b and rval == a) else rval
        if rval is None:
            return root.data if (root.data == a and lval == b) or (
                root.data == b and lval == a) else lval
        if (lval == a and rval == b) or (lval == b and rval == a):
            return root.data
        return None

    def lca_iter(root: Node, a: int, b: int) -> int:
        apath = TreeUtils.findpath(root, a)
        bpath = TreeUtils.findpath(root, b)
        if not apath or not bpath:
            return None
        lpar = None
        for apar, bpar in zip(apath, bpath):
            if apar != bpar:
                return lpar
            lpar = apar.data
        return lpar

    def size(root: Node) -> int:
        if root is None:
            return 0
        return 1 + TreeUtils.size(root.left) + TreeUtils.size(root.right)

    def height(root: Node) -> int:
        if root is None:
            return 0
        return 1 + max(TreeUtils.height(root.left), TreeUtils.height(root.right))

    def is_bst(root: Node, low: int, high: int) -> bool:
        if root is None:
            return True
        if low is not None and root.data < low:
            return False
        if high is not None and root.data >= high:
            return False
        if root.left is not None and root.left.data >= root.data:
            return False
        if root.right is not None and root.right.data < root.data:
            return False
        return TreeUtils.is_bst(root.left, low, root.data) and TreeUtils.is_bst(
            root.right, root.data, high)

    def _value_range(root: Node):
        if root == None:
            return (True, 0, None, None)
        lsmry = TreeUtils._value_range(root.left)
        rsmry = TreeUtils._value_range(root.right)
        if not lsmry[0] or not rsmry[0]:
            return (False, max(lsmry[1], rsmry[1]))
        if (lsmry[3] is None or lsmry[3] < root.data) and (
            rsmry[2] is None or root.data <= rsmry[2]):
            return (True, 1+lsmry[1]+rsmry[1],
                root.data if lsmry[2] is None else lsmry[2],
                root.data if rsmry[3] is None else rsmry[3])
        return (False, max(lsmry[1], rsmry[1]), None, None)

    def largest_bst(root: Node) -> int:
        return TreeUtils._value_range(root)[1]
