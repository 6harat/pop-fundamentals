from typing import List


def counting_sort(arr: List[int], rstart: int, rend: int):
    vlength = rend - rstart + 1
    varr = [0] * vlength
    for a in arr:
        varr[a - rstart] += 1
    sarr = []
    for idx, v in enumerate(varr):
        if v > 0:
            sarr.extend([idx + rstart] * v)
    return sarr
