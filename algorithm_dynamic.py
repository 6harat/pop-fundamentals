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