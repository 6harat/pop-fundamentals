from dataclasses import dataclass
import math
from typing import Callable, List


@dataclass
class LazyPropagationSegmentTree:
    func: Callable[[int, int], int]
    values: List[int]

    def __post_init__(self):
        n = len(self.values)
        index_size = pow(2, math.ceil(math.log(n, 2)) + 1) - 1
        index = [None] * index_size
        delta = [0] * index_size
        self._fill(index, 0, 0, n - 1)

        self._n = n
        self._index_size = index_size
        self._index = index
        self._delta = delta

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

    def _update_child_delta(self, jump, delta):
        if jump + 2 >= self._index_size:
            return
        if self._index[jump + 1] is not None:
            self._delta[jump + 1] += delta
        if self._index[jump + 2] is not None:
            self._delta[jump + 2] += delta

    def _query(self, iptr, ilow, ihigh, qlow, qhigh, delta) -> int:
        ndelta = self._delta[iptr] + delta
        if ilow > qhigh or ihigh < qlow:
            self._delta[iptr] = ndelta
            return None

        self._index[iptr] += ndelta
        self._delta[iptr] = 0
        jump, split = 2 * iptr, (ihigh + ilow) // 2
        if ilow >= qlow and ihigh <= qhigh:
            self._update_child_delta(jump, ndelta)
            return self._index[iptr]

        lval = self._query(jump + 1, ilow, split, qlow, qhigh, ndelta)
        rval = self._query(jump + 2, split + 1, ihigh, qlow, qhigh, ndelta)
        if lval is None:
            return rval
        if rval is None:
            return lval
        return self.func(lval, rval)

    def range_query(self, low, high) -> int:
        if low > high or low >= self._n:
            return None
        high = min(high, self._n - 1)
        return self._query(0, 0, self._n - 1, low, high, 0)

    def _update(self, iptr, ilow, ihigh, ulow, uhigh, delta):
        if ilow > uhigh or ihigh < ulow:
            return

        ndelta = self._delta[iptr] + delta
        self._delta[iptr] = 0
        jump, split = 2 * iptr, (ihigh + ilow) // 2
        if ilow >= ulow and ihigh <= uhigh:
            self._index[iptr] += ndelta
            self._update_child_delta(jump, ndelta)
            return

        self._update(jump + 1, ilow, split, ulow, uhigh, ndelta)
        self._update(jump + 2, split + 1, ihigh, ulow, uhigh, ndelta)
        self._index[iptr] = self.func(self._index[jump + 1],
                                      self._index[jump + 2])

    def range_update(self, low, high, delta):
        if low > high or low >= self._n:
            return
        high = min(high, self._n - 1)
        self._update(0, 0, self._n - 1, low, high, delta)


st = LazyPropagationSegmentTree(min, [4, 2, -1, 8, 3, 5, 7, 9, 20, 1, 12])
