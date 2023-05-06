
arr = [1,2,5,3,7,8,6,4]


def merge_sort(arr, start, end):
    if start >= end:
        return
    
    nums = end - start + 1
    pivot = (start + end)//2
    lstart, lstop = start, pivot
    rstart, rstop = pivot+1, end

    merge_sort(arr, lstart, lstop)
    merge_sort(arr, rstart, rstop)

    idx = 0
    buf = [None]*nums
    while lstart <= lstop and rstart <= rstop:
        if arr[lstart] <= arr[rstart]:
            buf[idx] = arr[lstart]
            lstart += 1
        else:
            buf[idx] = arr[rstart]
            rstart += 1
        idx += 1
    while lstart <= lstop:
        buf[idx] = arr[lstart]
        lstart += 1
        idx += 1
    while rstart <= rstop:
        buf[idx] = arr[rstart]
        rstart += 1
        idx += 1
    
    for idx in range(nums):
        arr[start + idx] = buf[idx]
