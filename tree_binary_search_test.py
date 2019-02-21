from tree_binary_search import (
    BinarySearchTree as bst,
    IterativeTraversal as itv,
    RecursiveTraversal as rtv
)

def getTree():
    tree = bst(20)
    tree.insert(12)
    tree.insert(8)
    tree.insert(29)
    tree.insert(15)
    tree.insert(41)
    tree.insert(59)
    tree.insert(31)
    return tree

if __name__ == '__main__':
    tree = getTree()