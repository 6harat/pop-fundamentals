def num_ways_to_represent_number_as_sum_consecutive_natural_numbers(n):
    """
    ref: https://www.geeksforgeeks.org/count-ways-express-number-sum-consecutive-numbers/
    """
    get_start_num = lambda l: (n - ( (l*(l+1))/2 ) )/(l+1)
    check_further = lambda l: l*(l+1) < 2*n
    l, opt = 1, 0
    while check_further(l):
        start_num = get_start_num(l)
        if start_num - int(start_num) == 0.0:
            opt += 1
        l += 1
    return opt

def longest_consecutive_sub_array_with_sum_atmost_k():
    """
    ref: https://www.geeksforgeeks.org/longest-subarray-sum-elements-atmost-k/
    """
    pass