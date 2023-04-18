from tree_binary_search import (
    BinarySearchTree as bst,
    StandardTraversal as stv,
    CustomTraversal as ctv,
    TreeBuilder as tbd
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


#             20
#     12              29
# 8       15              41
#                     31      59