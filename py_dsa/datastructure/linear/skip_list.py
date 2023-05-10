from collections import deque
from dataclasses import dataclass, field
import random
from typing import Deque, List


@dataclass
class Node:
    data: int
    next: 'Node' = field(repr=False)
    down: 'Node' = field(repr=False)


class SkipList:
    _sentinel = object()

    def __init__(self, seed: int, values: List[int]) -> None:
        self._random = random.Random(seed)
        self._head: Node = Node(SkipList._sentinel, None, None)
        for val in values:
            self.insert(val)

    def search(self, data: int) -> bool:
        vcurr = self._head
        while vcurr is not None:
            hprev, hcurr = None, vcurr
            while hcurr is not None:
                if hcurr.data is SkipList._sentinel or hcurr.data < data:
                    hprev = hcurr
                    hcurr = hcurr.next
                elif hcurr.data == data:
                    return True
                else:
                    break
            vcurr = hprev.down
        return False

    def insert(self, data: int) -> None:
        vstack: Deque[Node] = deque()
        vcurr = self._head
        while vcurr is not None:
            hprev, hcurr = None, vcurr
            while hcurr is not None:
                if hcurr.data is SkipList._sentinel or hcurr.data < data:
                    hprev = hcurr
                    hcurr = hcurr.next
                else:
                    break
            vstack.append(hprev)
            vcurr = hprev.down

        prev = vstack.pop()
        curr = Node(data, prev.next, None)
        prev.next = curr
        down = curr
        while self._should_elevate():
            if vstack:
                prev = vstack.pop()
                curr = Node(data, prev.next, down)
                prev.next = curr
            else:
                curr = Node(data, None, down)
                nhead = Node(SkipList._sentinel, curr, self._head)
                self._head = nhead
            down = curr

    def _should_elevate(self) -> bool:
        return self._random.random() < 0.5

    def prettyprint(self) -> None:
        self._print_level(self._head)

    def _print_level(self, head: Node) -> Deque[Node]:
        if head.down is None:
            queue: Deque[Node] = deque()
            while head is not None:
                queue.append(head)
                if head.data == SkipList._sentinel:
                    print("#", end="\t")
                else:
                    print(head.data, end="\t")
                head = head.next
            print()
            return queue

        down_level = self._print_level(head.down)
        queue: Deque[Node] = deque()
        while head is not None and down_level:
            el = down_level.popleft()
            if head.down is el:
                queue.append(head)
                if head.data == SkipList._sentinel:
                    print("#", end="\t")
                else:
                    print(head.data, end="\t")
                head = head.next
            else:
                queue.append(" ")
                print(" ", end="\t")
        print()
        return queue


sk = SkipList(23, [3, 2, 8, 6, 9, 13, 1, 3, 4, 79, 15, 7])
sk.prettyprint()
