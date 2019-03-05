arr = [6, 7, 1, 3, 8, 2, 4]

def max_sum_with_no_consecutive_elements(arr):
    """
    also known as stickler thief problem
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

def egg_dropping_problem(num_eggs, num_floors):
    mx = [ [0]*num_floors for _ in range(num_eggs) ]
    i = 0
    while i < num_eggs:
        j = 0
        while j < num_floors:
            if i == 0:
                mx[i][j] = j+1
    pass
