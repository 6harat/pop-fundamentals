test_pattern = 'acacabacacabacacac'
exp_ptable = [-1, -1, 0, 1, 2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3]

def minimum_edit_distance():
    """
    ref: 
    """
    pass
    
def construct_ptable(pattern):
    """
    ptable: prefix table
    ref: https://www.youtube.com/watch?v=KG44VoDtsAA
    determine lps: longest prefix which is same as suffix
    string    a  c  a  c  a  b  a  c  a  c  a  b  a  c  a  c  a  c
    ptable   -1 -1  0  1  2 -1  0  1  2  3  4  5  6  7  8  9 10  3
    """
    len_pattern = 0 if pattern is None else len(pattern)
    ptable = [-1]*len_pattern
    i, j = 0, 1
    while j < len_pattern:
        if pattern[i] == pattern[j]:
            ptable[j] = i
            i += 1
            j += 1
        elif i == 0:
            j += 1
        else:
            i = ptable[i-1] + 1
    return ptable

t1, p1 = 'ababcabcabababd', 'ababd'

def kmp(text, pattern):
    """
    kmp: knuth-morris-pratt
    ref: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
         https://www.youtube.com/watch?v=GTJr8OvyEVQ
    time_complexity: O(n+m)
    """
    len_text = 0 if text is None else len(text)
    len_pattern = 0 if pattern is None else len(pattern)

    if len_pattern > len_text:
        return None

    ptable = construct_ptable(pattern)
    i, j = 0, -1
    while i < len_text and j < len_pattern - 1:
        if text[i] == pattern[j+1]:
            i += 1
            j += 1
        elif j == -1:
            i += 1
        else:
            j = ptable[j]
    
    if j == len_pattern-1:
        return i - len_pattern
    
    return None

def rabin_karp():
    """
    ref: https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
    """
    pass

def finite_state_automation():
    """
    ref: https://www.geeksforgeeks.org/finite-automata-algorithm-for-pattern-searching/
    """
    pass

def boyer_moore():
    """
    ref: https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
    """
    pass

def ukkonen():
    """
    ref: 
    """
    pass

def zvalues():
    """
    ref: https://www.youtube.com/watch?v=CpZh4eF8QBw&list=PLrmLmBdmIlpvm7VaC0NTR27A_3i2sU3zd&index=3
    """
    pass

def manacher():
    """
    ref: https://www.youtube.com/watch?v=V-sEwsca1ak&index=2&list=PLrmLmBdmIlpvxhscYQdvfFNWU_pdkG5de
    """
    pass

def aho_corasick():
    """
    ref: https://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/
    """
    pass

def lis():
    """
    lis: longest increasing subsequence
    ref: https://www.geeksforgeeks.org/lis-using-segment-tree/
    """
    pass

def lce():
    """
    lce: longest common extension
    ref: https://www.geeksforgeeks.org/longest-common-extension-lce-set-1-introduction-and-naive-method/
         https://www.geeksforgeeks.org/longest-common-extension-lce-set-2-reduction-rmq/
         https://www.geeksforgeeks.org/longest-common-extension-lce-set-3-segment-tree-method/
    """
    pass