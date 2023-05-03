from typing import Callable, List


class BinaryHeap:
    def __init__(self, cmp: Callable[[int, int], int], values: List[int]):
        self.cmp = cmp
        self._n = len(values)
        self._index = values[:]
        for idx in range(self._n-1, -1, -1):
            self._heapify_down(idx)

    def _heapify_down(self, idx):
        lpidx = self._n//2
        while idx < lpidx:
            lidx = 2*idx + 1
            ridx = 2*idx + 2
            midx = idx
            if lidx < self._n and self.cmp(self._index[midx], self._index[lidx]) > 0:
                midx = lidx
            if ridx < self._n and self.cmp(self._index[midx], self._index[ridx]) > 0:
                midx = ridx
            if midx != idx:
                tmp = self._index[midx]
                self._index[midx] = self._index[idx]
                self._index[idx] = tmp
                idx = midx
            else:
                return

    def _heapify_up(self, idx):
        pidx = (idx-1)//2
        while idx > 0 and self.cmp(self._index[pidx], self._index[idx]) > 0:
            tmp = self._index[pidx]
            self._index[pidx] = self._index[idx]
            self._index[idx] = tmp
            idx = pidx
            pidx = (idx-1)//2

    def peek(self) -> int:
        if not self._index:
            return None
        return self._index[0]

    def pop(self) -> int:
        if not self._index:
            return None
        el = self._index[0]
        self._n -= 1
        if self._n == 0:
            self._index.pop()
            return el

        self._index[0] = self._index.pop()
        self._heapify_down(0)
        return el

    def push(self, data: int):
        self._index.append(data)
        self._n += 1
        self._heapify_up(self._n-1)

    def replace(self, data: int):
        pass
