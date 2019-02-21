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

    def search(self, val):
        curr_node = self.root
        while curr_node is not None and curr_node.data != val:
            curr_node = curr_node.left if curr_node.data > val else curr_node.right
        return curr_node
    
    def delete(self, val):
        prnt_node = None
        srch_node = self.root
        while srch_node is not None and srch_node.data != val:
            prnt_node = srch_node
            srch_node = srch_node.left if srch_node.data > val else srch_node.right
        
        if srch_node is None:
            raise ValueError('Value to be deleted not found')
        elif srch_node.left is None and srch_node.right is None:
            if prnt_node is None:
                self.root = None
            elif prnt_node.left == srch_node:
                prnt_node.left = None
            else:
                prnt_node.right = None
        elif srch_node.left is not None:
            curr_node = srch_node.left
            if curr_node.right is None:
                srch_node.data = curr_node.data
                srch_node.left = curr_node.left
                curr_node.left = None
            else:
                while curr_node.right.right is not None:
                    curr_node = curr_node.right
                srch_node.data = curr_node.right.data
                repl_node = curr_node.right
                curr_node.right = repl_node.left
                repl_node.left = None
        else:
            curr_node = srch_node.right
            if curr_node.left is None:
                srch_node.data = curr_node.data
                srch_node.right = curr_node.right
                curr_node.right = None
            else:
                while curr_node.left.left is not None:
                    curr_node = curr_node.left
                srch_node.data = curr_node.left.data
                repl_node = curr_node.left
                curr_node.left = repl_node.right
                repl_node.right = None

class RecursiveTraversal(object):
    """
    traverses a tree using recursion
    """
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
    """
    traverses a tree using additional storage (queue/stack)
    """
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

class ThreadedTraversal(object):
    """
    traverses a tree without the need of additional storage or recursion
    ref: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
    """
    @staticmethod    
    def level_order_traversal(root:Node):
        pass
    
    @staticmethod
    def pre_order_traversal(root:Node):
        pass
    
    @staticmethod
    def in_order_traversal(root:Node):
        pass

    @staticmethod
    def post_order_traversal(root:Node):
        pass

class NonThreadedTraversal(object):
    """
    traverses a tree without the need of threads, additional storage or recursion
    ref: https://www.geeksforgeeks.org/inorder-non-threaded-binary-tree-traversal-without-recursion-or-stack/
    """
    @staticmethod    
    def level_order_traversal(root:Node):
        pass
    
    @staticmethod
    def pre_order_traversal(root:Node):
        pass
    
    @staticmethod
    def in_order_traversal(root:Node):
        pass

    @staticmethod
    def post_order_traversal(root:Node):
        pass

class TrivialTraversal(object):
    @staticmethod
    def zig_zag_traversal(root:Node):
        pass
    
    @staticmethod
    def boundary_traversal(root:Node):
        pass

    @staticmethod
    def diagonal_traversal(root:Node):
        pass

class TreeRetrieval(object):
    @staticmethod
    def from_in_order_and_pre_order(in_order, pre_order):
        pass

    @staticmethod
    def from_in_order_and_post_order(in_order, post_order):
        pass

    @staticmethod
    def from_in_order_and_level_order(in_order, level_order):
        pass
