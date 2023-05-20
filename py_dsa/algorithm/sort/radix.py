import math
from typing import List


def radix_sort(arr: List[int]):
    num_digits = max_digits(max(arr))
    tmp_2darr = [list(range(len(arr)))]
    div_arr = arr[:]
    for d in range(num_digits - 1):
        bucket_arr = [[] for _ in range(10)]
        for tarr in tmp_2darr:
            for idx in tarr:
                div = div_arr[idx]
                bucket_idx = div % 10
                bucket_arr[bucket_idx].append(idx)
                div_arr[idx] = div // 10
        tmp_2darr = bucket_arr
    sorted_arr = []
    for tarr in tmp_2darr:
        for idx in tarr:
            sorted_arr.append(arr[idx])
    return sorted_arr


def max_digits(val):
    return math.ceil(math.log10(val))
