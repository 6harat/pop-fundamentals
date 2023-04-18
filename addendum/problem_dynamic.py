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
     
adv: https://www.youtube.com/watch?v=krZI60lKPek
also read more theory about parent pointers in detail which helps us
get the path to follow to get the optimized solution.
"""

def fibonacci():
    """
    ref: https://www.youtube.com/watch?v=OQ5jsbhAv_M
    """
    pass

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
         https://www.youtube.com/watch?v=ocZMDMZwhCY
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

lis_arr = [3, 4, -1, 0, 6, 2, 3]
def longest_increasing_subsequence(arr):
    """
    ref: https://www.youtube.com/watch?v=CE2b_-XfVDk
    """
    larr = len(arr)
    mtx = [1]*larr
    j, i = 0, 1
    while i < larr:
        if arr[j] < arr[i]:
            mtx[i] = max(mtx[i], mtx[j]+1)
        j += 1
        if i == j:
            i += 1
            j = 0
    return max(mtx)

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

def word_break_problem():
    """
    ref: https://www.youtube.com/watch?v=WepWFGxiwRs
    """
    pass

mje_arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
def minimum_jumps_to_reach_end(arr):
    """
    ref: https://www.youtube.com/watch?v=cETfFsSTGJI
    handle edge cases where arr: [0, ...] or [1, 0, ...] in which case it will be impossible
    """
    larr = len(arr)
    jump_arr = [None]*larr
    indx_arr = [None]*larr
    j, i = 0, 1
    jump_arr[0] = 0 # initialize base case
    while i < larr:
        if j + arr[j] >= i and (jump_arr[i] is None or jump_arr[j]+1 < jump_arr[i]) :
            jump_arr[i] = jump_arr[j]+1
            indx_arr[i] = j
        j += 1
        if i == j:
            i += 1
            j = 0
    # change the below code to return the proper indices rather than indx_arr
    return (jump_arr[-1], indx_arr)

def box_stacking_problem():
    """
    ref: https://www.youtube.com/watch?v=9mod_xRB-O0
    """
    pass

def staircase_problem():
    """
    ref: https://www.youtube.com/watch?v=CFQk7OQO_xM
    recursion relation is: 
        F(n) = F(n-1) + F(n-2)          , if you can take 1 or 2 steps at a time
        F(n) = F(n-1) + F(n-2) + F(n-3) , if you can take 1, 2 or 3 steps at a time
    """
    pass

def minimum_cost_path():
    """
    ref: https://www.youtube.com/watch?v=lBRtnuxg-gU
    arr = [
        [1, 3, 5, 8],
        [4, 2, 1, 7],
        [4, 3, 2, 3]
    ]
    opt = 12
    """
    pass

def palindrome_partitioning():
    """
    ref: https://www.youtube.com/watch?v=lDYIvtBVmgo
    """
    pass

def number_of_ways_to_traverse_matrix():
    """
    ref: https://www.youtube.com/watch?v=krZI60lKPek
    given a matrix and the starting point as (0,0) and right, up being the possible directions,
    find out the number of ways in which the point (m, n) can be reached
    x   x   x   x   m,n         1   7   28  84  210
    x   x   x   x   x           1   6   21  56  126
    x   x   x   x   x           1   5   15  35  70
    x   x   x   x   x     =>    1   4   10  20  35
    x   x   x   x   x           1   3   6   10  15
    x   x   x   x   x           1   2   3   4   5
    0,0 x   x   x   x           0   1   1   1   1

    opt = 210
    """
    pass

def number_of_inversions_for_adjacent_swaps():
    """
    ref: https://www.youtube.com/watch?v=Vj5IOD7A6f8
         for count the optimal algo takes O(n*log n) time
         for enumeration the optimal algo takes O(n*n) time
    """
    pass


def weighted_job_scheduling_problem():
    """
    ref: https://www.youtube.com/watch?v=cr6Ip0J9izc
    """
    pass

def find_list_of_possible_words_from_letter_in_matrix():
    """
    aka: boggle_solver
    ref: https://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver
    """
    pass