"""
links: 
    https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
"""

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
    def merge_sort_3way(vals, asc=True):
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
    def quick_sort_3way(vals, asc=True):
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

    @staticmethod
    def tim_sort(vals, asc=True):
        """
        ref: https://www.geeksforgeeks.org/timsort/
             http://svn.python.org/projects/python/trunk/Objects/listsort.txt
             https://en.wikipedia.org/wiki/Exponential_search
             https://gitlab.gnome.org/GNOME/libgee/blob/master/gee/timsort.vala
             https://hackernoon.com/timsort-the-fastest-sorting-algorithm-youve-never-heard-of-36b28417f399
        """
        pass

class EsotericComparisonSort(object):
    @staticmethod
    def intro_sort(vals, asc=True):
        """
        ref: https://en.wikipedia.org/wiki/Introsort
        """
        pass

    @staticmethod
    def cartesian_tree_sort(vals, asc=True):
        pass

    @staticmethod
    def splay_sort(vals, asc=True):
        pass

    @staticmethod
    def tree_sort(vals, asc=True):
        pass

    @staticmethod
    def shell_sort(vals, asc=True):
        pass

    @staticmethod
    def cube_sort(vals, asc=True):
        pass

    @staticmethod
    def cycle_sort(vals, asc=True):
        pass

    @staticmethod
    def library_sort(vals, asc=True):
        pass

    @staticmethod
    def patience_sort(vals, asc=True):
        pass

    @staticmethod
    def smooth_sort(vals, asc=True):
        pass

    @staticmethod
    def strand_sort(vals, asc=True):
        pass

    @staticmethod
    def tournament_sort(vals, asc=True):
        pass

    @staticmethod
    def cocktail_sort(vals, asc=True):
        pass

    @staticmethod
    def comb_sort(vals, asc=True):
        pass

    @staticmethod
    def gnome_sort(vals, asc=True):
        pass

    @staticmethod
    def unshuffle_sort(vals, asc=True):
        pass

    @staticmethod
    def franceschini_sort(vals, asc=True):
        pass

    @staticmethod
    def block_sort(vals, asc=True):
        pass

    @staticmethod
    def odd_even_sort(vals, asc=True):
        pass

    @staticmethod
    def sleep_sort(vals, asc=True):
        pass

    @staticmethod
    def tag_sort(vals, asc=True):
        pass

class NonComparisonSort(object):
    @staticmethod
    def counting_sort(vals, asc=True):
        pass

    @staticmethod
    def bucket_sort(vals, asc=True):
        if not vals:
            return vals

        if any(not 0<=v<=1 for v in vals):
            raise ValueError('values should be constrained to 0 <= value <= 1')

        buckets = [ [] for _ in range(10) ]
        for v in vals:
            buckets[int(v * 10)].append(v)
        
        return [ 
            nums for bucket in (
                asc and buckets or buckets[::-1]
            ) for nums in NaiveSort.insertion_sort_iterative(
                bucket, asc
            ) 
        ]

    @staticmethod
    def radix_sort_lsd(vals, asc=True):
        pass

    @staticmethod
    def radix_sort_msd(vals, asc=True):
        pass

    @staticmethod
    def pigeonhole_sort(vals, asc=True):
        pass

    @staticmethod
    def spread_sort(vals, asc=True):
        pass

    @staticmethod
    def burst_sort(vals, asc=True):
        pass

    @staticmethod
    def flash_sort(vals, asc=True):
        pass

    @staticmethod
    def postman_sort(vals, asc=True):
        pass

class NearlySorted(object):
    """
    ref: https://www.geeksforgeeks.org/nearly-sorted-algorithm/
         https://www.geeksforgeeks.org/sort-an-almost-sorted-array-where-only-two-elements-are-swapped/
    """
    pass

class ExternalSort(object):
	"""
	ref: https://en.wikipedia.org/wiki/External_sorting
		 https://en.wikipedia.org/wiki/External_memory_algorithm
		 https://en.wikipedia.org/wiki/Median_of_medians
		 https://www.geeksforgeeks.org/external-sorting/
		 https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
		 https://www.geeksforgeeks.org/merge-k-sorted-arrays-set-2-different-sized-arrays/
		 https://stackoverflow.com/questions/20802396/how-external-merge-sort-algorithm-works
		 https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/ExternalSort.html
		 http://www.csbio.unc.edu/mcmillan/Media/Comp521F10Lecture17.pdf
		 http://web.eecs.utk.edu/~bvz/cs302/notes/replacement_selection.html
		 https://stackoverflow.com/questions/16326689/replacement-selection-sort-v-selection-sort
		 https://en.wikipedia.org/wiki/In-place_algorithm
		 http://www.gvpcew.ac.in/LN-CSE-IT-22-32/CSE-IT/2-Year/22-ADS/ADS-AUK-UNIT-1.pdf
	"""
	@staticmethod
	def kway_merge_sort():
		pass
	
	@staticmethod
	def merge_sort():
		pass

	@staticmethod
	def distribution_sort():
		pass

	@staticmethod
	def replacemnet_sort():
		pass

class QuantumSort(object):
    pass

class NSFWSort(object):
    @staticmethod
    def bead_sort(vals, asc=True):
        pass

    @staticmethod
    def pancake_sort(vals, asc=True):
        pass

    @staticmethod
    def spaghetti_sort(vals, asc=True):
        pass

    @staticmethod
    def network_sort(vals, asc=True):
        pass

    @staticmethod
    def bitonic_sort(vals, asc=True):
        pass

    @staticmethod
    def bogo_sort(vals, asc=True):
        pass

    @staticmethod
    def stooge_sort(vals, asc=True):
        pass
