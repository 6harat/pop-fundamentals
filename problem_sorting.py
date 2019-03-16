def num_inversions_in_array(arr):
    """
    ref: https://www.geeksforgeeks.org/counting-inversions/
    """
    pass

def minimum_num_swaps_to_sort_array(arr):
    """
    ref: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
    """
    larr = len(arr)
    pos_arr = list(enumerate(arr))
    pos_arr.sort(key=lambda it:it[1])
    visited = [False]*larr
    opt = 0
    for i in range(larr):
        if visited[i] or pos_arr[i][0] == i:
            continue
        cyc_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = pos_arr[j][0]
            cyc_size += 1
        if cyc_size > 0:
            opt += cyc_size - 1
    return opt

def minimum_num_adjacent_swaps_to_sort_array():
    """
    ref: https://www.geeksforgeeks.org/number-swaps-sort-adjacent-swapping-allowed/
    """
    pass