import math

a = [6, 7, 1, 2]
b = [6, 7, 1, 2, 4, 5, -1, 8]

class SegmentTree(object):
    """
    ref: https://www.geeksforgeeks.org/segment-tree-efficient-implementation/
         https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
         https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/
         https://www.geeksforgeeks.org/iterative-segment-tree-range-minimum-query/
         https://www.geeksforgeeks.org/segment-tree-xor-given-range/
         https://www.geeksforgeeks.org/segment-trees-product-of-given-range-modulo-m/
         https://www.geeksforgeeks.org/segment-tree-set-2-range-maximum-query-node-update/

         https://www.youtube.com/watch?v=ZBHKZF5w4YU

         advanced_topics:
            https://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/
            https://www.geeksforgeeks.org/range-update-query-chessboard-pieces/
            https://www.geeksforgeeks.org/reconstructing-segment-tree/
            https://www.geeksforgeeks.org/two-dimensional-segment-tree-sub-matrix-sum/
            https://www.geeksforgeeks.org/levelwise-alternating-gcd-lcm-nodes-segment-tree/
            https://www.geeksforgeeks.org/levelwise-alternating-xor-operations-segment-tree/
            https://www.geeksforgeeks.org/counting-inversions-in-an-array-using-segment-tree/
            https://www.geeksforgeeks.org/efficiently-design-insert-delete-median-queries-set/

    """
    def __init__(self, inp, func):
        self.inp = inp
        self.func = func
        self._inp_size = len(self.inp)
        adjusted_size = pow(2, math.ceil(math.log(self._inp_size, 2)))
        self._seg_size = adjusted_size * 2 - 1
        self.seg = [None]*self._seg_size
        print(self.seg)
        SegmentTree._construct_tree(self.inp, self.seg, 0, self._inp_size-1, 0, self.func)
    
    @staticmethod
    def _construct_tree(inp, seg, low, high, pos, fn):
        # print('low: {}, high: {}, pos: {}, inp: {}, seg: {}'.format(low, high, pos, inp, seg))
        if low == high:
            seg[pos] = inp[low]
            return
        mid = (low + high)//2
        l_pos, r_pos = 2*pos+1, 2*pos+2
        SegmentTree._construct_tree(inp, seg, low, mid, l_pos, fn)
        SegmentTree._construct_tree(inp, seg, mid+1, high, r_pos, fn)
        seg[pos] = fn(seg[l_pos], seg[r_pos])

    @staticmethod
    def _query(seg, qlow, qhigh, low, high, pos, fn):
        # print('qlow: {}, qhigh: {}, low: {}, high: {}, pos: {}'.format(
        #     qlow, qhigh, low, high, pos
        # ))
        if qlow <= low and high <= qhigh:
            return seg[pos]
        elif high < qlow or qhigh < low:
            return None

        mid = (low + high)//2
        lval = SegmentTree._query(seg, qlow, qhigh, low, mid, 2*pos+1, fn)
        rval = SegmentTree._query(seg, qlow, qhigh, mid+1, high, 2*pos+2, fn)
        if lval == None:
            return rval
        elif rval == None:
            return lval
        else:
            return fn(lval, rval)

    def query(self, qlow, qhigh):
        return SegmentTree._query(
            self.seg, 
            qlow, qhigh, 
            0, self._inp_size - 1, 
            0, self.func
        )

    def __repr__(self):
        return 'SegmentTree(seg={})'.format(self.seg)

class EulerTourTree(object):
    """
    ref: https://www.geeksforgeeks.org/euler-tour-subtree-sum-using-segment-tree/
    """
    pass

class IntervalTree(object):
    """
    a type of segment tree which holds intervals
    ref: https://www.geeksforgeeks.org/interval-tree/
    """
    pass

class PersistentSegmentTree(object):
    """
    ref: https://www.geeksforgeeks.org/persistent-segment-tree-set-1-introduction/
    """
    pass