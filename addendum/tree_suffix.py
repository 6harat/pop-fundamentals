"""
farach's algorithm for creating a suffix tree:
     https://www.cs.rutgers.edu/~farach/pubs/Suffix.pdf
"""

class SuffixTree(object):
    """
    ref: https://www.geeksforgeeks.org/pattern-searching-using-suffix-tree/
         https://www.geeksforgeeks.org/suffix-tree-application-1-substring-check/
         https://www.geeksforgeeks.org/suffix-tree-application-2-searching-all-patterns/
         https://www.geeksforgeeks.org/suffix-tree-application-3-longest-repeated-substring/
         https://www.geeksforgeeks.org/suffix-tree-application-4-build-linear-time-suffix-array/
         https://www.geeksforgeeks.org/suffix-tree-application-5-longest-common-substring-2/
         https://www.geeksforgeeks.org/suffix-tree-application-6-longest-palindromic-substring/
    """
    pass

class UkkonenTree(object):
    """
    ref: https://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-1/
         https://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-2/
         https://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-3/
         https://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-4/
         https://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-5/
         https://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-6/

     also read about theoretical difference between:
          Implicit Suffix Tree: all suffixes are not represented in the tree 
               (case when last character is already a part of the string)
          True Suffix Tree: when last character is unique, all suffixes are represented in the tree


     rule 1: if an edge does not exist create one
     rule 2: if an edge exist but char does not exist, append the character to the last
     rule 3: if an edge as well as the char exist, jump to next execution phase

     optimization tricks:
     + trick 1: skip/count; edge label compression
     + trick 2: rule 3 is show-stopper
     + trick 3: global end for leaves
    """
    pass


class EulerTourTree(object):
    """
    ref: https://www.geeksforgeeks.org/euler-tour-subtree-sum-using-segment-tree/
    """
    pass

class IntervalTree(object):
    """
    a type of segment tree which holds intervals
    ref: https://www.geeksforgeeks.org/interval-tree/
    """
    pass

class PersistentSegmentTree(object):
    """
    ref: https://www.geeksforgeeks.org/persistent-segment-tree-set-1-introduction/
    """
    pass
