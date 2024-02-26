"""
Problem Link: https://www.hackerrank.com/challenges/balanced-forest/problem
"""
import math
import os
import random
import re
import sys


class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children
        self.sum = None
        self.visited = 0


def construct_tree(c, edges):
    nodes = [ TreeNode(val, set()) for val in c ]
    for (x, y) in edges:
        nodes[x-1].children.add(nodes[y-1])
        nodes[y-1].children.add(nodes[x-1])
    return nodes[0]


def compute_sum(root: TreeNode, visit_mark: int):
    stack = (root, None)
    while stack:
        node = stack[0]
        if node.visited != visit_mark:
            node.visited = visit_mark
            for child in node.children:
                child.children.remove(node)
                stack = (child, stack)
        else:
            stack = stack[-1]
            node.sum = node.val + sum(( 
                child.sum for child in node.children ))


def dfs(root: TreeNode, visit_mark: int):
    stack = (root, None)
    visited_node_sum = set()
    visited_comp_sum = set()
    min_sum_subtree = math.ceil(root.sum / 3)
    best_case_opt = (min_sum_subtree * 3) - root.sum
    opt = math.inf

    def has_twin(node: TreeNode, pool: set[TreeNode]):
        return node.sum >= min_sum_subtree and node.sum in pool

    def has_ysib(node: TreeNode, pool: set[TreeNode]):
        return node.sum >= min_sum_subtree and (root.sum - (2 * node.sum)) in pool
    
    def has_osib(node: TreeNode, pool: set[TreeNode]):
        delta = root.sum - node.sum
        sum_subtree = delta // 2
        return not (delta & 1) and sum_subtree >= min_sum_subtree and sum_subtree in pool

    while stack:
        node = stack[0]
        comp_sum = root.sum - node.sum
        if node.visited != visit_mark:
            node.visited = visit_mark
            for child in node.children:
                stack = (child, stack)
            visited_comp_sum.add(comp_sum)
            if has_twin(node, visited_node_sum) or has_ysib(node, visited_node_sum):
                opt = min(opt, (node.sum * 3) - root.sum)
            elif has_osib(node, visited_node_sum):
                opt = min(opt, (root.sum - (3 * node.sum)) // 2)
        else:
            stack = stack[-1]
            if has_twin(node, visited_comp_sum) or has_ysib(node, visited_comp_sum):
                opt = min(opt, (node.sum * 3) - root.sum)
            elif has_osib(node, visited_comp_sum):
                opt = min(opt, (root.sum - (3 * node.sum)) // 2)
            visited_comp_sum.remove(comp_sum)
            visited_node_sum.add(node.sum)

        if opt == best_case_opt:
            break

    if opt is math.inf:
        opt = -1
    return opt


def balancedForest(c, edges, n):
    # base condition check
    if n < 2 or (n == 2 and c[0] != c[1]):
        return -1

    root = construct_tree(c, edges)
    compute_sum(root, visit_mark=1)

    opt = dfs(root, visit_mark=2)
    return opt


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())
        c = list(map(int, input().rstrip().split()))
        edges = [list(map(int, input().rstrip().split())) for _ in range(n - 1)]

        print(balancedForest(c, edges, n))
