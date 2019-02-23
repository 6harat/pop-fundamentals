import enum
import random

from heap_binary import (
    BinaryHeap as bheap
)

class Pivot(enum.Enum):
    FIRST = lambda lval: 0
    LAST = lambda lval: lval-1
    RANDOM = lambda lval: random.randrange(lval)
    MEDIAN = lambda lval: 0

def swap(opt, i, j):
    if i == j or opt[i] == opt[j]:
        return
    tmp = opt[i]
    opt[i] = opt[j]
    opt[j] = tmp

def cmp(asc, a, b):
    if asc:
        return a < b
    else:
        return a > b

class NaiveSort(object):
    @staticmethod
    def bubble_sort_recursive(vals, asc=True):
        """
        ref: https://www.geeksforgeeks.org/recursive-bubble-sort/
        """
        pass

    @staticmethod
    def bubble_sort_iterative(vals, asc=True):
        if not vals:
            return vals
        
        opt = vals[:]
        lval, is_not_sorted = len(vals), True
        while is_not_sorted:
            is_not_sorted, idx = False, 0
            while idx < lval-1:
                if not cmp(asc, opt[idx], opt[idx+1]):
                    swap(opt, idx, idx+1)
                    is_not_sorted = True
                idx += 1
        return opt

    @staticmethod
    def selection_sort_recursive(vals, asc=True):
        pass

    @staticmethod
    def selection_sort_iterative(vals, asc=True):
        if not vals:
            return vals

        opt = vals[:]
        idx, lval = 0, len(vals)
        while idx < lval:
            ptr_idx, curr_idx = idx, idx + 1
            while curr_idx < lval:
                if cmp(asc, opt[curr_idx], opt[ptr_idx]):
                    ptr_idx = curr_idx
                curr_idx += 1
            swap(opt, ptr_idx, idx)
            idx += 1
        return opt

    @staticmethod
    def insertion_sort_recursive(vals, asc=True):
        """
        ref: https://www.geeksforgeeks.org/recursive-insertion-sort/
        """
        pass

    @staticmethod
    def insertion_sort_iterative(vals, asc=True):
        if not vals:
            return vals
        
        opt = vals[:]
        idx, lval = 1, len(vals)
        while idx < lval:
            ptr_idx = idx
            while ptr_idx > 0 and cmp(asc, opt[ptr_idx], opt[ptr_idx-1]):
                swap(opt, ptr_idx, ptr_idx-1)
                ptr_idx -= 1
            idx += 1
        return opt
    
class ComparisonSort(object):
    @staticmethod
    def merge_sort_recursive(vals, asc=True, lidx=None, ridx=None):
        if not vals:
            return vals
        
        lidx = lidx if lidx is not None else 0
        pass
    
    @staticmethod
    def merge_sort_iterative(vals, asc=True):
        pass

    @staticmethod
    def quick_sort_recursive(vals, asc=True, pivot=Pivot.LAST):
        if not vals:
            return vals
        
        lval = len(vals)
        if lval == 1:
            return vals

        pvt_idx = pivot(lval)
        left_vals, equal_vals, right_vals = [], [], []
        for v in vals:
            if v == vals[pvt_idx]: equal_vals.append(v)
            elif cmp(asc, v, vals[pvt_idx]): left_vals.append(v)
            else: right_vals.append(v)
        
        return ComparisonSort.quick_sort_recursive(
            left_vals, asc=asc, pivot=pivot
        ) + equal_vals + ComparisonSort.quick_sort_recursive(
            right_vals, asc=asc, pivot=pivot
        )

    @staticmethod
    def quick_sort_iterative(vals, asc=True):
        pass

    @staticmethod
    def heap_sort_recursive(vals, asc=True):
        pass

    @staticmethod
    def heap_sort_iterative(vals, asc=True):
        if not vals:
            return vals

        hp = bheap(vals, is_max=not asc)
        opt = []
        while not hp.is_empty():
            opt.append(hp.pop())
        return opt

class TrivialSort(object):
    @staticmethod
    def counting_sort(vals, asc=True):
        pass

    @staticmethod
    def radix_sort(vals, asc=True):
        pass

    @staticmethod
    def bucket_sort(vals, asc=True):
        pass

class EsotericSort(object):
    pass

class ExternalSort(object):
    pass