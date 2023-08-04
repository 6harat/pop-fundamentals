from collections import deque
from dataclasses import dataclass
from typing import List


@dataclass
class Operation:
    items: List[str]
    pointer: int


def copyAndSwap(items: List[str], idx_a: int, idx_b: int):
    transformed = items[:]
    tmp = transformed[idx_a]
    transformed[idx_a] = transformed[idx_b]
    transformed[idx_b] = tmp
    return transformed


def permute(items: List[str]):
    num_items = len(items)
    op_q = deque([Operation(items, 0)])
    opt = deque([])
    while op_q:
        op = op_q.popleft()
        if op.pointer == num_items - 1:
            opt.append(op.items)
            continue
        for i in range(op.pointer, num_items):
            op_q.append(
                Operation(copyAndSwap(op.items, op.pointer, i),
                          op.pointer + 1))
    return list(opt)


if __name__ == "__main__":
    input = ["A", "B", "C"]
    opt = permute(input)
    print("\n".join((str(i) for i in opt)))
