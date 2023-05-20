from typing import List


def bucket_sort(arr: List[float]):
    bucket_arr = [[] for _ in range(10)]
    for a in arr:
        idx = int(a * 10)
        bucket_arr[idx].append(a)

    for bucket in bucket_arr:
        sarr = []
        for val in bucket:
            pass
