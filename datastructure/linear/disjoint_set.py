from dataclasses import dataclass
from typing import List

@dataclass
class Node:
    data: str
    parent: int
    rank: int

@dataclass
class DisjointSet:
    values: List[str]

    def __post_init__(self):
        bijection = dict()
        ctr = len(self.values)
        association = [None]*ctr
        for idx in range(ctr):
            val = self.values[idx]
            bijection[val] = idx
            association[idx] = Node(val, idx, 0)

        self._ctr = ctr
        self._bijection = bijection
        self._association = association

    def union(self, val1: str, val2: str) -> None:
        ctr1 = self._bijection.get(val1)
        ctr2 = self._bijection.get(val2)
        if ctr1 is None or ctr2 is None:
            return
        pctr1 = self._find_set_with_compression(ctr1)
        pctr2 = self._find_set_with_compression(ctr2)
        if pctr1 == pctr2:
            return
        node1 = self._association[pctr1]
        node2 = self._association[pctr2]
        if node1.rank < node2.rank:
            node1.parent = pctr2
            return
        
        if node1.rank == node2.rank: # increment only if ranks were same
            node1.rank += 1
        node2.parent = pctr1

    def find_set(self, val: str) -> str:
        ctr = self._bijection.get(val)
        if ctr is None:
            return None
        pctr = self._find_set_with_compression(ctr)
        return self._association[pctr].data
    
    def _find_set_with_compression(self, ctr: int) -> int:
        node = self._association[ctr]
        if ctr == node.parent:
            return ctr
        node.parent = self._find_set_with_compression(node.parent)
        return node.parent

    def make_set(self, val: str) -> None:
        self.values.append(val)
        self._bijection[self._ctr] = val
        self._association.append(Node(self._ctr, 0))
        self._ctr += 1

ds = DisjointSet(["hello", "world", "foo", "bar", "roger", "that", "fog", "light"])
