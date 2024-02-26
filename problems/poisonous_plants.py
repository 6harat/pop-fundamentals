"""
Problem Link: https://www.hackerrank.com/challenges/poisonous-plants/problem
"""
import math
import os
import random
import re
import sys


def poisonousPlants_bruteForce(n, p):
    opt = 0
    plants = p
    while plants:
        has_dels = False
        prev = plants[0]
        plants_new = [prev]
        for val in plants[1:]:
            if prev >= val:
                plants_new.append(val)
            else:
                has_dels = True
            prev = val
        if not has_dels:
            return opt
        plants = plants_new
        opt += 1
    return opt


class Node:
    def __init__(self, val):
        self.val = val
        self.day = 0
    def __repr__(self) -> str:
        return f"(v={self.val},d={self.day})"


def poisonousPlants(n, p):
    stack = (Node(p[0]), None)
    idx = 1

    def prune(stack, pval):
        print("stack: ", stack)
        top = stack[0]
        stack = stack[-1]
        while stack and (pval is None or top.val >= pval) and top.val > stack[0].val:
            stack[0].day = max(stack[0].day + 1, top.day)
            top = stack[0]
            stack = stack[-1]
        return (top, stack)

    while stack and idx < n:
        pval = p[idx]
        if pval > stack[0].val:
            stack = (Node(pval), stack)
        else:
            stack = prune(stack, pval)
            stack = (Node(pval), stack)
        idx += 1

    stack = prune(stack, None)
    max_days = 0
    while stack:
        top = stack[0]
        max_days = max(max_days, top.day)
        stack = stack[-1]
    return max_days


if __name__ == '__main__':
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))[:n]

    print(poisonousPlants_bruteForce(n, p))
    print(poisonousPlants(n, p))
