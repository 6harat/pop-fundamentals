import math

class Array(object):
    pass

class DifferenceArray(object):
    """
    ref: https://www.geeksforgeeks.org/difference-array-range-update-query-o1/
                   0    1    2    3    4    5    6    7
    orig_arr = [   2,   4,  54,  12,   3,   8,  42,  91]
    diff_arr = [   2,   2,  50, -42,  -9,   5,  34,  49]

    operation: add 7 to objects from idx 2 to 5
        updt_arr = [   2,   2,  57, -42,  -9,   5,  27,  49]
        cmpt_arr = [   2,   4,  61,  19,  10,  15,  42,  91]

    time_complexity:
        update: O(1)
        print_array: O(n)
    space_complexity: O(n)

    todo:
        add/remove element: ???
    """
    pass

arr = [ 4, 6, 1, 5, 7, 3]
brr = [ 4, 6, 1, 5, 7, 12, -2, 14, 13, 8]

class SparseTable(object):
    """
    ref: https://www.geeksforgeeks.org/sparse-table/
         https://www.geeksforgeeks.org/range-sum-query-using-sparse-table/
         https://www.geeksforgeeks.org/range-minimum-query-for-static-array/
    
    constraints:
        - array, arr is immutable
        - function, f is associative, i.e. f(a, b, c) = f( f(a, b), c) = f(a, f(b, c))

    methodology:
        sparse_table[i][j] = f(arr[i], arr[i+1], ... , arr[i+pow(2, j)-1])
        num_rows = n
        num_cols = log(n) + 1
    illustration:
        arr = [ 4, 6, 1, 5, 7, 3]
        sparse_table = 
           r/c  0  1  2
            0   4  4  1
            1   6  1  1
            2   1  1  1
            3   5  5
            4   7  3
            5   3
    """
    def __init__(self, inp, func):
        self.inp = inp
        self.func = func
        self.len_row = len(inp)
        self.len_col = int(math.log2(self.len_row) + 1)
        self.sp_table = self._create_table()
        pass
    
    def _create_table(self):
        sp_table = list(map(lambda i: [self.inp[i]], range(self.len_row)))
        j = 0
        while j < self.len_col:
            i = 0
            num_elements = self.len_row - 2**(j+1)
            while i <= num_elements:
                sp_table[i].append(self.func(sp_table[i][j], sp_table[i + 2**j][j]))
                i += 1
            j += 1
        self.j = j
        return sp_table

    def rmq(self, low, high):
        """
        rmq: range minimum/maximum query
        constraint: range overlapping should not affect the result of self.func - max, min 
                    (but not for sum where the overlapped elements would be counted twice)
        time_complexity: O(1)
        """
        num = high - low + 1
        col = int(math.log2(num))
        row1 = low
        row2 = low + num - 2**col
        return self.func(self.sp_table[row1][col], self.sp_table[row2][col])

    def query(self, low, high):
        """
        this is a generic query function
        constraint: works for all self.func which are associative
        time_complexity: O(log n)
        """
        num = high - low + 1
        opt = None
        while num > 0:
            curr = int(math.log2(num))
            if opt == None:
                opt = self.sp_table[low][curr]
            else:
                opt = self.func(opt, self.sp_table[low][curr])
            curr = 2**curr
            num -= curr
            low += curr
        return opt

    def __repr__(self):
        return 'SparseTable(sp_table={})'.format(self.sp_table)

class Stack(object):
    pass

class Queue(object):
    pass

class Deque(object):
    pass

class CircularQueue(object):
    pass

class LinkedList(object):
    """
    ref: https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
    """
    pass

class DoublyLinkedList(object):
    pass

class XORLinkedList(object):
    """
    ref: https://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-1/
    """
    pass

class CircularLinkedList(object):
    pass

class DoublyCircularLinkedList(object):
    pass

class UnrolledLinkedList(object):
    pass

class BiotonicList(object):
    pass

class SkipList(object):
    pass

class SuffixArray(object):
    """
    ref: https://www.geeksforgeeks.org/suffix-array-set-1-introduction/
    """
    pass

class EnhancedSufixArray(object):
    pass

class SparseSuffixArray(object):
    pass

class SelfOrganizingList(object):
    """
    ref: https://www.geeksforgeeks.org/self-organizing-list-set-1-introduction/
    """
    pass

class SparseMatrix(object):
    """
    ref: https://www.geeksforgeeks.org/sparse-matrix-representation/
         https://www.geeksforgeeks.org/sparse-matrix-representations-using-list-lists-dictionary-keys/
         https://www.geeksforgeeks.org/sparse-matrix-representations-set-3-csr/
         https://www.geeksforgeeks.org/operations-sparse-matrices/
    """
    pass