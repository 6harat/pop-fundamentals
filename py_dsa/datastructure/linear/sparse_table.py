from dataclasses import dataclass
import math
from typing import Callable, List


@dataclass
class SparseTable:
    func: Callable[[int, int], int]
    values: List[int]

    def __post_init__(self):
        rows = len(self.values)
        cols = int(math.log2(rows)+1)
        index = [[idx] for idx in range(rows)]

        cmul = 1
        for cidx in range(1, cols):
            jump = cmul
            cmul *= 2
            for ridx in range(rows-cmul+1):
                idx1 = index[ridx][cidx-1]
                idx2 = index[ridx+jump][cidx-1]
                val1 = self.values[idx1]
                val2 = self.values[idx2]
                val = self.func(val1, val2)
                index[ridx].append(idx1 if val == val1 else idx2)
        self._rows = rows
        self._cols = cols
        self._index = index

    def range_query(self, low, high):
        if low > high or low >= self._rows:
            return None
        high = min(high, self._rows-1)
        num = high - low + 1
        col = int(math.log2(num))
        row1, row2 = low, high+1-2**col
        idx1, idx2 = self._index[row1][col], self._index[row2][col]
        val1, val2 = self.values[idx1], self.values[idx2]
        return self.func(val1, val2)

@dataclass
class SparseTableExt:
    func: Callable[[int, int], int]
    identity: int
    values: List[int]

    def __post_init__(self):
        rows = len(self.values)
        cols = int(math.log2(rows)+1)
        result = []
        result = [[self.func(self.identity, val)] for val in self.values]

        cmul = 1
        for cidx in range(1, cols):
            jump = cmul
            cmul *= 2
            for ridx in range(rows-cmul+1):
                val1 = result[ridx][cidx-1]
                val2 = result[ridx+jump][cidx-1]
                val = self.func(val1, val2)
                result[ridx].append(val)
        self._rows = rows
        self._cols = cols
        self._result = result

    def range_query(self, low, high):
        if low > high or low >= self._rows:
            return None
        high = min(high, self._rows-1)
        opt = self.identity
        while high-low+1 > 0:
            curr = int(math.log2(high-low+1))
            opt = self.func(opt, self._result[low][curr])
            curr = 2**curr
            low += curr
        return opt

stab = SparseTable(min, [4, 2, -1, 8, 3, 5, 7, 9, 20, 1, 12])
stabext = SparseTableExt(lambda a, b: a+b, 0, [4, 2, -1, 8, 3, 5, 7, 9, 20, 1, 12])
