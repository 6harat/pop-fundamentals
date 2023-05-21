from collections import defaultdict
from curses import set_tabsize
from dataclasses import dataclass
import random
from typing import List

from py_dsa.datastructure.linear.disjoint_set import DisjointSet


@dataclass
class Edge:
    source: int
    target: int
    weight: int


@dataclass
class UndirectedGraph:
    vertices: List[int]
    edges: List[Edge]

    def __post_init__(self):
        self._vnum = len(self.vertices)
        self._enum = len(self.edges)
        self._random = random.Random(13)

    def dfs(self):
        pass

    def bfs(self):
        pass

    def djikstra_mst(self):
        pass

    def kruskal_mst(self):
        set_tracker = DisjointSet(self.vertices)
        sorted_edges = sorted(self.edges, key=lambda edge: edge.weight)
        required_edges = self._vnum - 1
        mst = [None] * required_edges
        midx, eidx = 0, 0
        while midx < required_edges and eidx < self._enum:
            edge = sorted_edges[eidx]
            source_set = set_tracker.find_set(edge.source)
            target_set = set_tracker.find_set(edge.target)
            if source_set != target_set:
                mst[midx] = edge
                set_tracker.union(edge.source, edge.target)
                midx += 1
            eidx += 1
        return None if midx != required_edges else (mst,
                                                    sum((edge.weight
                                                         for edge in mst)))

    def prim_mst(self):
        sorted_edges = sorted(self.edges, key=lambda edge: edge.weight)
        vset = {self._random.randint(0, self._vnum - 1)}
        required_edges = self._vnum - 1
        mst = [None] * required_edges
        midx = 0
        while midx < required_edges and sorted_edges:
            eidx, edge = next(
                ((eidx, edge) for eidx, edge in enumerate(sorted_edges)
                 if (edge.source in vset) ^ (edge.target in vset)),
                (None, None))
            if edge is None:
                return None
            sorted_edges.pop(eidx)
            vset.add(edge.source)
            vset.add(edge.target)
            mst[midx] = edge
            midx += 1
        return None if midx != required_edges else (mst,
                                                    sum((edge.weight
                                                         for edge in mst)))

    def boruvka_mst(self):
        pass

    def reverse_delete_mst(self):
        pass

    def karger_klein_tarjan_mst(self):
        pass

    def chazelle_mst(self):
        pass

    def pettie_ramachandran_mst(self):
        pass


graph1 = UndirectedGraph(vertices=list(range(0, 4)),
                         edges=[
                             Edge(0, 1, 10),
                             Edge(0, 2, 6),
                             Edge(0, 3, 5),
                             Edge(1, 3, 15),
                             Edge(2, 3, 4)
                         ])

graph2 = UndirectedGraph(vertices=list(range(0, 6)),
                         edges=[
                             Edge(0, 1, 2),
                             Edge(0, 2, 5),
                             Edge(0, 3, 2),
                             Edge(0, 4, 3),
                             Edge(1, 3, 0),
                             Edge(2, 3, 1),
                             Edge(2, 4, 6),
                             Edge(3, 4, 4),
                             Edge(3, 5, 8)
                         ])

graph3 = UndirectedGraph(vertices=list(range(0, 9)),
                         edges=[
                             Edge(0, 1, 6),
                             Edge(0, 3, 3),
                             Edge(1, 2, 4),
                             Edge(1, 4, 2),
                             Edge(2, 5, 12),
                             Edge(3, 4, 1),
                             Edge(3, 6, 8),
                             Edge(4, 5, 7),
                             Edge(4, 7, 9),
                             Edge(5, 8, 10),
                             Edge(6, 7, 11),
                             Edge(7, 8, 5)
                         ])

graph4 = UndirectedGraph(vertices=list(range(0, 6)),
                         edges=[
                             Edge(0, 2, 10),
                             Edge(0, 3, 1),
                             Edge(2, 3, 1),
                             Edge(2, 4, 10),
                             Edge(3, 5, 1),
                             Edge(4, 5, -5)
                         ])
