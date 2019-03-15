"""
dynamic_programming is comprised of:
    - careful brute force
    - recursion + memoization + guessing (take the best guess at each step)
    - shortest path in some DAG
core rule: for memoization to work in DP, the subproblem dependencies should be acyclic/
i.e. the subproblem should not depend on the solution to itself leading to an infinte loop.
time_complexity = num_subproblem * time_per_subproblem (treating recursive calls as O(1))
steps involved in solving dynamic programming problem:
    - define subproblems            (num_subproblems)
    - guess part of solution        (num_choices)
    - relate suproblem solutions    (relationship such as min{..., ...} and it must be acyclic)
    - recurse and memoize           (build DP table bottom-up or use recursive function calls)
    - solve original problem        
ref: https://www.youtube.com/watch?v=OQ5jsbhAv_M
     https://www.youtube.com/watch?v=ENyox7kNKeY
     https://www.youtube.com/watch?v=ocZMDMZwhCY
     https://www.youtube.com/watch?v=tp4_UXaVyx8
"""


arr = [6, 7, 1, 3, 8, 2, 4]

def max_sum_with_no_consecutive_elements(arr):
    """
    aka: stickler thief problem
    ref: https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/
    """
    d1, d2 = arr[0], max(arr[:2])
    idx, len_arr = 2, len(arr)
    while idx < len_arr:
        curr = max(d1 + arr[idx], d2)
        d1 = d2
        d2 = curr
        idx += 1
    return d2


def egg_dropping_problem(num_eggs, num_floors):
    mx = [ [0]*num_floors for _ in range(num_eggs) ]
    i = 0
    while i < num_eggs:
        j = 0
        while j < num_floors:
            if i == 0:
                mx[i][j] = j+1
    pass


def knapsack_problem():
    """
    ref: https://www.youtube.com/watch?v=8LusJS5-AGo
    """
    pass

def subset_sum_problem():
    """
    ref: https://www.youtube.com/watch?v=s6FhG--P7z0
    """
    pass

def longest_common_substring():
    """
    ref: https://www.youtube.com/watch?v=BysNXJHzCEs
    """
    pass

def longest_common_subsequence():
    """
    ref: https://www.youtube.com/watch?v=NnD96abizww
    """
    pass


text = 'agbdba'
def longest_palindromic_subsequence(text):
    """
    subsequence - chars can have gaps between them
    ref: https://www.youtube.com/watch?v=_nCsPn7_OgI
    """
    if not text:
        return 0

    n, sel_len = len(text), 0
    opt = [ [None]*n for _ in range(n) ]
    while sel_len < n:
        i = 0
        while i + sel_len < n:
            col_pos = i + sel_len
            if i == col_pos:
                opt[i][col_pos] = 1
            elif text[i] == text[col_pos]:
                opt[i][col_pos] = opt[i+1][col_pos-1] + 2
            else:
                opt[i][col_pos] = max(opt[i][col_pos-1], opt[i+1][col_pos])
            i += 1
        sel_len += 1
    return opt[0][n-1]

def matrix_chain_multiplication():
    """
    ref: https://www.youtube.com/watch?v=vgLJZMUfnsU
    """
    pass

def coin_changing_problem():
    """
    ref: https://www.youtube.com/watch?v=Y0ZqKpToTic
    """
    pass

def coin_changing_problem_efficient():
    """
    a space efficient version which only requires O(n) space
    where n is the total to be achieved using the coins
    ref: https://www.youtube.com/watch?v=NJuKJ8sasGk
    """
    pass

def coin_changing_num_ways_to_get_total():
    """
    ref: https://www.youtube.com/watch?v=_fgjrs570YE
    todo: see if there is an efficient solution exist which requires O(n) space only
          where n is the total to be achieved using the coins
    """
    pass

def cutting_rod_problem():
    """
    ref: https://www.youtube.com/watch?v=IRwVmTmN6go
    """
    pass

def cutting_rod_problem_efficient():
    """
    ref: https://www.youtube.com/watch?v=IRwVmTmN6go
    """
    pass