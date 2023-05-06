from dataclasses import dataclass
import math
from typing import Callable, List


@dataclass
class SegmentTree:
    func: Callable[[int, int], int]
    values: List[int]

    def __post_init__(self):
        n = len(self.values)
        index_size = pow(2, math.ceil(math.log(n, 2)) + 1) - 1
        index = [None] * index_size
        self._fill(index, 0, 0, n - 1)

        self._n = n
        self._index_size = index_size
        self._index = index

    def _fill(self, index, iptr, low, high):
        if low == high:
            opt = self.values[low]
            index[iptr] = opt
            return opt
        jump, split = 2 * iptr, (high + low) // 2
        lopt = self._fill(index, jump + 1, low, split)
        ropt = self._fill(index, jump + 2, split + 1, high)
        opt = self.func(lopt, ropt)
        index[iptr] = opt
        return opt

    def _query(self, iptr, ilow, ihigh, qlow, qhigh) -> int:
        if ilow > qhigh or ihigh < qlow:
            return None
        if ilow >= qlow and ihigh <= qhigh:
            return self._index[iptr]
        jump, split = 2 * iptr, (ihigh + ilow) // 2
        lval = self._query(jump + 1, ilow, split, qlow, qhigh)
        rval = self._query(jump + 2, split + 1, ihigh, qlow, qhigh)
        if lval is None:
            return rval
        if rval is None:
            return lval
        return self.func(lval, rval)

    def range_query(self, low, high) -> int:
        if low > high or low >= self._n:
            return None
        high = min(high, self._n - 1)
        return self._query(0, 0, self._n - 1, low, high)

    def _update(self, iptr, ilow, ihigh, ulow, uhigh, ufunc):
        if ilow > uhigh or ihigh < ulow:
            return
        if ilow == ihigh:
            self._index[iptr] = ufunc(self._index[iptr])
            return

        jump, split = 2 * iptr, (ihigh + ilow) // 2
        self._update(jump + 1, ilow, split, ulow, uhigh, ufunc)
        self._update(jump + 2, split + 1, ihigh, ulow, uhigh, ufunc)

        self._index[iptr] = self.func(self._index[jump + 1],
                                      self._index[jump + 2])

    def range_update(self, low, high, ufunc):
        if low > high or low >= self._n:
            return
        high = min(high, self._n - 1)
        self._update(0, 0, self._n - 1, low, high, ufunc)


st = SegmentTree(min, [4, 2, -1, 8, 3, 5, 7, 9, 20, 1, 12])
