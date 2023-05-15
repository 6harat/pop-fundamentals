from dataclasses import dataclass
from typing import List


@dataclass
class DifferenceArray:
    values: List[int]

    def __post_init__(self):
        self._n = len(self.values)
        self._diffs = [0]*self._n

    def update(self, delta: int, start_idx: int, end_idx: int) -> None:
        last_idx = min(end_idx, self._n-1) + 1
        self._diffs[start_idx] += delta
        if last_idx < self._n:
            self._diffs[last_idx] -= delta

    def accumulate(self) -> List[int]:
        acc_values = self.values[:]
        carry = 0
        for idx in range(self._n):
            carry += self._diffs[idx]
            acc_values[idx] += carry
        return acc_values


da = DifferenceArray([3, 4, 1, 7, 8, 5, 9])
da.update(-3, 2, 5)
da.update(10, 0, 2)
da.update(-7, 4, 9)
