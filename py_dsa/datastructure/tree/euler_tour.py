from dataclasses import dataclass, field
from typing import Dict, List
from py_dsa.datastructure.linear.sparse_table import SparseTable


@dataclass
class Node:
    data: int
    children: List['Node'] = field(repr=False)


class EulerTourTree:

    def __init__(self, root: Node) -> None:
        self._key_ctr = 0
        self._visit_ctr = 0
        self._key_map: Dict[int, int] = {}
        self._data_map: Dict[int, int] = {}
        self._impressions: List[int] = []
        self._depths: List[int] = []
        self._nodes: List[int] = []
        self._dfs(root, 0)
        self._sparse_table = SparseTable(min, self._depths)

    def _dfs(self, root: Node, depth: int):
        if root is None:
            return

        self._visit(root, depth)
        if not root.children:
            return

        for child in root.children:
            self._dfs(child, depth + 1)
            self._visit(root, depth)

    def _visit(self, node: Node, depth: int):
        key = self._key_map.get(node.data)
        if key is None:
            key = self._key_ctr
            self._key_map[node.data] = key
            self._data_map[key] = node.data
            self._key_ctr += 1
            self._impressions.append(self._visit_ctr)
        else:
            self._impressions[key] = self._visit_ctr
        self._depths.append(depth)
        self._nodes.append(key)
        self._visit_ctr += 1

    def lca(self, data1: int, data2: int) -> int:
        key1, key2 = self._key_map.get(data1), self._key_map.get(data2)
        if key1 is None or key2 is None:
            return None

        impr1, impr2 = self._impressions[key1], self._impressions[key2]
        low_impr, high_impr = min(impr1, impr2), max(impr1, impr2)
        node_idx = self._sparse_table.range_query_idx(low_impr, high_impr)
        key = self._nodes[node_idx]
        data = self._data_map[key]
        return data


if __name__ == "__main__":
    tree1 = Node(10, [
        Node(15, [Node(3, [Node(5, None)]),
                  Node(6, None)]),
        Node(30, [Node(2, [Node(9, None), Node(8, None)])])
    ])

    etree = EulerTourTree(tree1)
