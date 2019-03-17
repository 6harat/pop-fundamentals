from tree_nodes import BinaryNode as Node

class AvlTree(object):
    """
    self-balancing binary tree. requires more rotations for insertion and deletion 
    in comparison to red-black trees but are more balanced than those.
    should be used when search is more frequent than insertion and deletion
    """
    @staticmethod
    def insert(root, key, record=None):
        if root is None:
            return Node(key, record=record, height=1)
        elif key < root.key:
            root.left = AvlTree.insert(root.left, key, record)
        else:
            root.right = AvlTree.insert(root.right, key, record)

        AvlTree.update_height(root)
        balance = AvlTree.get_balance(root)
        # print('balance: {} for root: {}'.format(balance, root))

        if balance > 1 and key < root.left.key:
            return AvlTree.right_rotate(root)
        
        if balance < -1 and key > root.right.key:
            return AvlTree.left_rotate(root)
        
        if balance > 1 and key > root.left.key:
            root.left = AvlTree.left_rotate(root.left)
            return AvlTree.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = AvlTree.right_rotate(root.right)
            return AvlTree.left_rotate(root)
    
        return root
    
    @staticmethod
    def get_height(root):
        return 0 if root is None else root.height

    @staticmethod
    def get_balance(root):
        return 0 if root is None else AvlTree.get_height(root.left) - AvlTree.get_height(root.right)

    @staticmethod
    def update_height(root):
        if root is None:
            return
        root.height = 1 + max(AvlTree.get_height(root.left), AvlTree.get_height(root.right))

    @staticmethod
    def left_rotate(root):
        new_root = root.right
        abd_child = new_root.left
        root.right = abd_child
        new_root.left = root
        AvlTree.update_height(root)
        AvlTree.update_height(new_root)
        return new_root

    @staticmethod
    def right_rotate(root):
        new_root = root.left
        abd_child = new_root.right
        root.left = abd_child
        new_root.right = root
        AvlTree.update_height(root)
        AvlTree.update_height(new_root)
        return new_root

    @staticmethod
    def pre_order(root, opt=None):
        if root is None:
            return
        if opt is None:
            opt = []
        opt.append(root.key)
        AvlTree.pre_order(root.left, opt)
        AvlTree.pre_order(root.right, opt)
        return opt

    @staticmethod
    def pre_order_iterative(root):
        if root is None:
            return
        opt, stack, curr_node = [], [], root
        while stack or curr_node:
            while curr_node is not None:
                opt.append(curr_node.key)
                stack.append(curr_node)
                curr_node = curr_node.left
            last_node = stack.pop()
            curr_node = last_node.right
        return opt

    @staticmethod
    def in_order_iterative(root):
        if root is None:
            return
        opt, stack, curr_node = [], [], root
        while stack or curr_node:
            while curr_node is not None:
                stack.append(curr_node)
                curr_node = curr_node.left
            last_node = stack.pop()
            opt.append(last_node.key)
            curr_node = last_node.right
        return opt
    
    @staticmethod
    def post_order_iterative_alt(root):
        if root is None:
            return
        opt, stack = [], [root]
        while stack:
            node = stack.pop()
            opt.append(node.key)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return opt[::-1]

    @staticmethod
    def post_order_iterative(root):
        if root is None:
            return
        opt, stack, curr_node = [], [], root
        while stack or curr_node:
            while curr_node is not None:
                opt.append(curr_node.key)
                stack.append(curr_node)
                curr_node = curr_node.right
            last_node = stack.pop()
            curr_node = last_node.left
        return opt[::-1]

    @staticmethod
    def level_order_iterative(root):
        if root is None:
            return
        opt, idx, size = [root], 0, 1
        while idx < size:
            curr = opt[idx]
            if curr.left is not None:
                size += 1
                opt.append(curr.left)
            if curr.right is not None:
                size += 1
                opt.append(curr.right)
            opt[idx] = curr.key
            idx += 1
        return opt

if __name__ == '__main__':
    root = None
    root = AvlTree.insert(root, 10) 
    root = AvlTree.insert(root, 20) 
    root = AvlTree.insert(root, 30) 
    root = AvlTree.insert(root, 40) 
    root = AvlTree.insert(root, 50) 
    root = AvlTree.insert(root, 25)
    root = AvlTree.insert(root, 35)