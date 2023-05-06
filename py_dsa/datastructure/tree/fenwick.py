from dataclasses import dataclass
from typing import List


@dataclass
class FenwickTree:
    values: List[int]

    def __post_init__(self):
        self._n = len(self.values)
        self._index = [0] * (self._n + 1)
        for idx, val in enumerate(self.values):
            self.update(idx, val)

    def sum(self, end: int) -> int:
        if end < 0:
            return None
        end = min(end + 1, self._n)
        opt = 0
        while end != 0:
            opt += self._index[end]
            end -= end & -end
        return opt

    def update(self, idx: int, delta: int) -> int:
        if idx < 0 or idx >= self._n:
            return
        idx += 1
        while idx <= self._n:
            self._index[idx] += delta
            idx += idx & -idx


fwt = FenwickTree([3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3])
