class BTree(object):
    """
    ref: https://stackoverflow.com/a/17103710/6687477
         https://www.geeksforgeeks.org/b-tree-set-1-introduction-2/
         https://www.geeksforgeeks.org/b-tree-set-1-insert-2/
         https://www.geeksforgeeks.org/b-tree-set-3delete/
         https://en.wikipedia.org/wiki/B-tree
         https://www.cs.cornell.edu/courses/cs3110/2012sp/recitations/rec25-B-trees/rec25.html
         https://medium.com/@vijinimallawaarachchi/all-you-need-to-know-about-deleting-keys-from-b-trees-9090f3334b5c
         http://www.mathcs.emory.edu/~cheung/Courses/554/Syllabus/3-index/B-tree=intro.html
    properties:
        minimum degree, `t`: depends upon disk block size
        number of keys, `num_keys` in nodes (except root node): t-1 <= num_keys <= 2t-1
        number of keys, `num_keys` in root node: 1 <= num_keys <= 2t-1
        number of children, num_child of a node: num_keys + 1
        keys in a node are stored in increasing sorted order
        child between two keys k1, k2 contains all the keys in the range [k1, k2]
    """
    pass

class BplusTree(object):
    pass

class BstarTree(object):
    pass

class MultiwaySearchTree(object):
    pass