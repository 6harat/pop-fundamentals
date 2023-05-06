from dataclasses import dataclass
from typing import List


@dataclass
class PrefixSumArray:
    values: List[int]

    def __post_init__(self):
        n = len(self.values)
        index = [0] * n
        csum = 0
        for idx in range(n):
            csum += self.values[idx]
            index[idx] = csum
        self._n = n
        self._index = index

    def sum(self, end: int) -> int:
        return self._index[end]


psa = PrefixSumArray([3, 2, 0, 6, 5, -1, 2])
