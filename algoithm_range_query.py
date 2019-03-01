from tree_nodes import BinaryNode as node

def linear():
    """
    greedy approach
    preprocess: O(1)
    evaluate: O(n)
    """
    pass

def dynamic_programming():
    """
    preprocess the entire data set
    preprocess: O(n^2)
    evaluate: O(1)
    """
    pass

def segment_tree():
    """
    preprocess the data sets in a tree with intervals
    preprocess: O(n)
    evaluate: O(logn)
    """
    pass

def sparse_table():
    """
    preprocess the data sets in batches of 2^n
    preprocess: O(n logn)
    evaluate: 
        O(1)    - if overlapping is acceptable
        O(logn) - if overlapping is not acceptable
    """
    pass

def create_tree():
    # create tree

        # left subtree
    n9 = node(9)
    n5 = node(5)
    n11 = node(11, n9, n5)
    n2 = node(2)
    n6 = node(6, n2, n11)

        # right subtree
    n7 = node(7)
    n13 = node(13, n7)
    n8 = node(8, right=n13)

        # root
    root = node(3, n6, n8)
    
    return root

def lowest_common_ancestor(root, n1, n2):
    """
    ref: https://www.youtube.com/watch?v=13m9ZCB8gjw
    preprocess the data sets
    preprocess: O(n)
    evaluate: O(1)
    """
    if root is None:
        return root

    if root.key == n1 or root.key == n2:
        return root.key
    
    lval = lowest_common_ancestor(root.left, n1, n2)
    if lval is not None and lval != n1 and lval != n2:
        return lval
    rval = lowest_common_ancestor(root.right, n1, n2)
    
    if (lval == n1 or lval == n2) and (rval == n1 or rval == n2):
        return root.key
    elif lval is not None:
        return lval
    else:
        return rval