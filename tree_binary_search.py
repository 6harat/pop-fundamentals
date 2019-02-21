from node_binary import BinaryNode as Node
from numbers import Real as numeric

class BinarySearchTree(object):
    def __init__(self, val=None):
        self.root = Node(val) if val is not None else None

    def insert(self, val):
        if not isinstance(val, numeric):
            raise ValueError('Can not insert non-numeric value')
        if self.root is None:
            self.root = Node(val)
            return
        curr_node = self.root
        while True:
            if curr_node.data > val:
                if curr_node.left is None:
                    curr_node.left = Node(val)
                    return
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = Node(val)
                    return
                else:
                    curr_node = curr_node.right

    def _search(self, val, curr_node=None):
        curr_node = curr_node or self.root
        prnt_node = None
        while curr_node is not None and curr_node.data != val:
            prnt_node = curr_node
            curr_node = curr_node.left if curr_node.data > val else curr_node.right
        return curr_node, prnt_node

    def search(self, val):
        return self._search(val)[0]
    
    def delete(self, val):
        srch_opt = self._search(val)


class RecursiveTraversal(object):
    @staticmethod    
    def level_order_traversal(root:Node):
        pass
    
    @staticmethod
    def pre_order_traversal(root:Node):
        if root is None:
            return []
        opt = [root.data]
        opt.extend(RecursiveTraversal.pre_order_traversal(root.left))
        opt.extend(RecursiveTraversal.pre_order_traversal(root.right))
        return opt
    
    @staticmethod
    def in_order_traversal(root:Node):
        if root is None:
            return []
        opt = RecursiveTraversal.in_order_traversal(root.left)
        opt.append(root.data)
        opt.extend(RecursiveTraversal.in_order_traversal(root.right))
        return opt

    @staticmethod
    def post_order_traversal(root:Node):
        if root is None:
            return []
        opt = RecursiveTraversal.post_order_traversal(root.left)
        opt.extend(RecursiveTraversal.post_order_traversal(root.right))
        opt.append(root.data)
        return opt

class IterativeTraversal(object):
    @staticmethod    
    def level_order_traversal(root:Node):
        if root is None:
            return []
        from collections import deque
        opt = []
        dq = deque()
        dq.append(root)
        while dq:
            curr_node = dq.popleft()
            if curr_node is not None:
                opt.append(curr_node.data)
                if curr_node.left is not None: dq.append(curr_node.left)
                if curr_node.right is not None: dq.append(curr_node.right)
        return opt
    
    @staticmethod
    def pre_order_traversal(root:Node):
        if root is None:
            return []
        stack, opt, curr_node = [], [], root
        while stack or curr_node:
            while curr_node is not None:
                opt.append(curr_node.data)
                stack.append(curr_node)
                curr_node = curr_node.left
            last_node = stack.pop()
            curr_node = last_node.right
        return opt
    
    @staticmethod
    def in_order_traversal(root:Node):
        if root is None:
            return []
        stack, opt, curr_node = [root], [], root.left
        while stack or curr_node:
            while curr_node is not None:
                stack.append(curr_node)
                curr_node = curr_node.left
            last_node = stack.pop()
            opt.append(last_node.data)
            curr_node = last_node.right
        return opt

    @staticmethod
    def post_order_traversal(root:Node):
        if root is None:
            return []
        stack, opt = [root], []
        while stack:
            last_node = stack.pop()
            opt.append(last_node.data)
            if last_node.left is not None:
                stack.append(last_node.left)
            if last_node.right is not None:
                stack.append(last_node.right)
        return opt[::-1]