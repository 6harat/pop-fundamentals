"""
total number of trees possible with n nodes: combinations(2n, n)/n+1
"""

from tree_nodes import BinaryNode as Node
from numbers import Real as numeric

class BinarySearchTree(object):
    """
    ref: https://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/
         https://www.geeksforgeeks.org/find-lca-in-binary-tree-using-rmq/
    """
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
            if curr_node.key > val:
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
        while curr_node is not None and curr_node.key != val:
            curr_node = curr_node.left if curr_node.key > val else curr_node.right
        return curr_node
    
    def delete(self, val):
        prnt_node = None
        srch_node = self.root
        while srch_node is not None and srch_node.key != val:
            prnt_node = srch_node
            srch_node = srch_node.left if srch_node.key > val else srch_node.right
        
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
                srch_node.key = curr_node.key
                srch_node.left = curr_node.left
                curr_node.left = None
            else:
                while curr_node.right.right is not None:
                    curr_node = curr_node.right
                srch_node.key = curr_node.right.key
                repl_node = curr_node.right
                curr_node.right = repl_node.left
                repl_node.left = None
        else:
            curr_node = srch_node.right
            if curr_node.left is None:
                srch_node.key = curr_node.key
                srch_node.right = curr_node.right
                curr_node.right = None
            else:
                while curr_node.left.left is not None:
                    curr_node = curr_node.left
                srch_node.key = curr_node.left.key
                repl_node = curr_node.left
                curr_node.left = repl_node.right
                repl_node.right = None
    @staticmethod
    def checkForEquality(xtree, ytree):
        if xtree ^ ytree:
            return False
        if xtree is None and ytree is None:
            return True
        pass

    def __eq__(self, that):
        return BinarySearchTree.checkForEquality(self, that)
    def __ne__(self, that):
        return not self.__eq__(that)
    
class StandardTraversal(object):
    """
    traverses a tree in level-order, pre-order, in-order or post-order
    """
    @staticmethod    
    def level_order_traversal_recursive(root:Node):
        # https://www.geeksforgeeks.org/level-order-tree-traversal/
        pass
    
    @staticmethod    
    def level_order_traversal_iterative(root:Node):
        if root is None:
            return []
        from collections import deque
        opt = []
        dq = deque()
        dq.append(root)
        while dq:
            curr_node = dq.popleft()
            if curr_node is not None:
                opt.append(curr_node.key)
                if curr_node.left is not None: dq.append(curr_node.left)
                if curr_node.right is not None: dq.append(curr_node.right)
        return opt

    @staticmethod
    def pre_order_traversal_recursive(root:Node):
        if root is None:
            return []
        opt = [root.key]
        opt.extend(StandardTraversal.pre_order_traversal_recursive(root.left))
        opt.extend(StandardTraversal.pre_order_traversal_recursive(root.right))
        return opt
    
    @staticmethod
    def pre_order_traversal_iterative(root:Node):
        if root is None:
            return []
        stack, opt, curr_node = [], [], root
        while stack or curr_node:
            while curr_node is not None:
                opt.append(curr_node.key)
                stack.append(curr_node)
                curr_node = curr_node.left
            last_node = stack.pop()
            curr_node = last_node.right
        return opt

    @staticmethod
    def in_order_traversal_recursive(root:Node):
        if root is None:
            return []
        opt = StandardTraversal.in_order_traversal(root.left)
        opt.append(root.key)
        opt.extend(StandardTraversal.in_order_traversal(root.right))
        return opt

    @staticmethod
    def in_order_traversal_iterative(root:Node):
        if root is None:
            return []
        stack, opt, curr_node = [root], [], root.left
        while stack or curr_node:
            while curr_node is not None:
                stack.append(curr_node)
                curr_node = curr_node.left
            last_node = stack.pop()
            opt.append(last_node.key)
            curr_node = last_node.right
        return opt

    @staticmethod
    def post_order_traversal_recursive(root:Node):
        if root is None:
            return []
        opt = StandardTraversal.post_order_traversal(root.left)
        opt.extend(StandardTraversal.post_order_traversal(root.right))
        opt.append(root.key)
        return opt

    @staticmethod
    def post_order_traversal_iterative(root:Node):
        if root is None:
            return []
        stack, opt = [root], []
        while stack:
            last_node = stack.pop()
            opt.append(last_node.key)
            if last_node.left is not None:
                stack.append(last_node.left)
            if last_node.right is not None:
                stack.append(last_node.right)
        return opt[::-1]

class ThreadedBinaryTree(object):
    """
    ref: https://www.geeksforgeeks.org/threaded-binary-tree-insertion/
    """
    pass
    
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

class CustomTraversal(object):
    @staticmethod
    def zig_zag_traversal_iterative_queue(root:Node):
        opt = []
        if root is None:
            return opt
        from collections import deque
        fwd, bwd = deque(), deque()
        fwd.append(root)
        while fwd or bwd:
            opt.extend(map(lambda n: n.key, fwd))
            while fwd:
                curr_node = fwd.popleft()
                if curr_node.left is not None:
                    bwd.append(curr_node.left)
                if curr_node.right is not None:
                    bwd.append(curr_node.right)
            opt.extend(map(lambda n: n.key, reversed(bwd)))
            while bwd:
                curr_node = bwd.popleft()
                if curr_node.left is not None:
                    fwd.append(curr_node.left)
                if curr_node.right is not None:
                    fwd.append(curr_node.right)
        return opt
    
    @staticmethod
    def zig_zag_traversal_iterative_stack(root:Node):
        """
        ref: https://www.geeksforgeeks.org/zig-zag-traversal-of-a-binary-tree-using-recursion/
             https://www.geeksforgeeks.org/reverse-zigzag-traversal-of-a-binary-tree/
        """
        opt = []
        if root is None:
            return opt
        curr_stack, next_stack = [], []
        curr_stack.append(root)
        append_left_then_right = True
        while curr_stack:
            while curr_stack:
                node = curr_stack.pop()
                opt.append(node.key)
                if append_left_then_right:
                    if node.left is not None:
                        next_stack.append(node.left)
                    if node.right is not None:
                        next_stack.append(node.right)
                else:
                    if node.right is not None:
                        next_stack.append(node.right)
                    if node.left is not None:
                        next_stack.append(node.left)
            append_left_then_right = not append_left_then_right
            temp_stack = curr_stack
            curr_stack = next_stack
            next_stack = temp_stack
        return opt

    @staticmethod
    def zig_zag_traversal_recursive(root:Node):
        pass

    @staticmethod
    def boundary_traversal(root:Node):
        opt = []
        if root is None:
            return opt
        opt.append(root.key)
        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        def left_boundary():
            curr_node = root.left
            left_nodes = []
            while curr_node is not None and not is_leaf(curr_node):
                left_nodes.append(curr_node.key)
                curr_node = curr_node.left
            return left_nodes
        def leaves_boundary():
            opt = []
            from collections import deque
            dq = deque()
            dq.append(root)
            while dq:
                curr_node = dq.popleft()
                if is_leaf(curr_node):
                    opt.append(curr_node.key)
                else:
                    if curr_node.left is not None:
                        dq.append(curr_node.left)
                    if curr_node.right is not None:
                        dq.append(curr_node.right)
            return opt
        def right_boundary():
            curr_node = root.right
            right_nodes = []
            while curr_node is not None and not is_leaf(curr_node):
                right_nodes.append(curr_node.key)
                curr_node = curr_node.right
            return right_nodes
        opt.extend(left_boundary())
        opt.extend(leaves_boundary())
        opt.extend(right_boundary()[::-1])
        return opt

    @staticmethod
    def diagonal_traversal(root:Node):
        """
        ref: https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/
        """
        pass

class TreeBuilder(object):
    @staticmethod
    def from_in_order_and_pre_order(in_order_seq, pre_order_seq):
        """
        ref: https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
        """
        if in_order_seq ^ pre_order_seq:
            raise ValueError('traversal sequences do not belong to the same tree')
        if not in_order_seq and not pre_order_seq:
            return BinarySearchTree()
        


    @staticmethod
    def from_in_order_and_post_order(in_order_seq, post_order_seq):
        pass

    @staticmethod
    def from_in_order_and_level_order(in_order_seq, level_order_seq):
        pass

class TraversalSequenceEvaluator(object):
    """
    identifies if the traversal sequence are of the same tree
    """
    pass

class Trivial:
    """
    additional algorithms that work on binary search tree
    """
    @staticmethod
    def optimal_binary_search_tree():
        """
        ref: https://www.youtube.com/watch?v=hgA4xxlVvfQ
        """
        pass
