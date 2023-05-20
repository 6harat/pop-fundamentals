from dataclasses import dataclass
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
        return None if midx != required_edges else mst

    def prim_mst(self):
        pass


graph1 = UndirectedGraph(vertices=[0, 1, 2, 3],
                         edges=[
                             Edge(0, 1, 10),
                             Edge(0, 2, 6),
                             Edge(0, 3, 5),
                             Edge(1, 3, 15),
                             Edge(2, 3, 4)
                         ])
