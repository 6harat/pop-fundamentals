test_pattern = 'acacabacacabacacac'
exp_ptable = [-1, -1, 0, 1, 2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3]

ipt = 'abcdef'
opt = 'azced'

def minimum_edit_distance(str_ipt, str_opt):
    """
    aka: wagner fischer algorithm/ levenshtein algorithm
    ref: https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
    """
    if not any([str_ipt, str_opt]):
        return 0
    elif str_ipt is None:
        return len(str_opt)
    elif str_opt is None:
        return len(str_ipt)
    
    len_ipt = len(str_ipt)
    len_opt = len(str_opt)
    mx = [ [0]*(len_ipt + 1) for _ in range(len_opt + 1) ]
    i = 0
    while i <= len_opt:
        j = 0
        while j <= len_ipt:
            if i == 0:
                mx[i][j] = j
            elif j == 0:
                mx[i][j] = i
            elif str_ipt[j-1] == str_opt[i-1]:
                mx[i][j] = mx[i-1][j-1]
            else:
                mx[i][j] = min(mx[i][j-1], mx[i-1][j], mx[i-1][j-1]) + 1
            j += 1
        i += 1
    return mx[-1][-1]

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
         https://www.youtube.com/watch?v=H4VrKHVG5qI&index=2&list=PLrmLmBdmIlpvm7VaC0NTR27A_3i2sU3zd
    time_complexity: O(mn)
    applications: 
        - document plagiarism
        - one text string and multiple patterns to be matched
    """
    pass

def z_box():
    """
    ref: https://ivanyu.me/blog/2013/10/15/z-algorithm/
         https://www.youtube.com/watch?v=CpZh4eF8QBw
    """
    pass

def finite_state_automation():
    """
    ref: https://www.geeksforgeeks.org/finite-automata-algorithm-for-pattern-searching/
    """
    pass

def boyer_moore_horspool():
    """
    ref: https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
    """
    pass

def baeza_yates_gonnet():
    """
    ref: https://en.wikipedia.org/wiki/Bitap_algorithm
    """
    pass

def ukkonen():
    """
    ref: 
    """
    pass

def manacher():
    """
    aka: longest palindromic substring
    substring - chars should be continuous
    ref: https://www.youtube.com/watch?v=V-sEwsca1ak&index=2&list=PLrmLmBdmIlpvxhscYQdvfFNWU_pdkG5de
    """
    pass

def aho_corasick():
    """
    ref: https://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/
    """
    pass

def longest_increasing_subsequence():
    """
    aka: lis - longest increasing subsequence
    ref: https://www.geeksforgeeks.org/lis-using-segment-tree/
    """
    pass

def longest_common_extension():
    """
    aka: lce - longest common extension
    ref: https://www.geeksforgeeks.org/longest-common-extension-lce-set-1-introduction-and-naive-method/
         https://www.geeksforgeeks.org/longest-common-extension-lce-set-2-reduction-rmq/
         https://www.geeksforgeeks.org/longest-common-extension-lce-set-3-segment-tree-method/
    """
    pass

def myers_diff():
    """
    ref: https://blog.jcoglan.com/2017/02/12/the-myers-diff-algorithm-part-1/
    """
    pass

def hunt_mcilroy_diff():
    """
    ref: https://en.wikipedia.org/wiki/Hunt%E2%80%93McIlroy_algorithm
    """
    pass

def levenshtein_distance():
    """
    ref: https://en.wikipedia.org/wiki/Levenshtein_distance#Iterative_with_full_matrix
    """
    pass

def text_justification():
    """
    ref: https://www.youtube.com/watch?v=ENyox7kNKeY
    """
    pass