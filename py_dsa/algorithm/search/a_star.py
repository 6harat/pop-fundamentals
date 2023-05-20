from dataclasses import dataclass
import math
from typing import List, Tuple


@dataclass
class Point:
    r: int
    c: int


@dataclass
class Move:
    p: Point
    lcost: float


UNBLOCKED_TILE = 0
BLOCKED_TILE = 1
SOURCE_TILE = 2
TARGET_TILE = 3

LEFT_DIR = 0
RIGHT_DIR = 1
UP_DIR = 2
DOWN_DIR = 3


def a_star_search(board: List[List[int]]) -> List[Point]:
    rlen, clen = len(board), len(board[0])
    source_coords, target_coords = _find_coords(board, rlen, clen)
    path = _dfs(source_coords, None, target_coords, board, rlen, clen)
    return path


def _dfs(curr: Point, parent: Point, dest: Point, board: List[List[int]],
         rlen: int, clen: int):
    if curr == dest:
        return [curr]
    lpoint = Point(curr.r, curr.c - 1) if curr.c > 0 else None
    lmove = _create_move(lpoint, parent, dest, board)
    rpoint = Point(curr.r, curr.c + 1) if curr.c < clen - 1 else None
    rmove = _create_move(rpoint, parent, dest, board)
    upoint = Point(curr.r - 1, curr.c) if curr.r > 0 else None
    umove = _create_move(upoint, parent, dest, board)
    dpoint = Point(curr.r + 1, curr.c) if curr.r < rlen - 1 else None
    dmove = _create_move(dpoint, parent, dest, board)

    moves: List[Move] = [
        move for move in (lmove, rmove, umove, dmove) if move is not None
    ]
    sorted_moves = sorted(moves, key=lambda m: m.lcost, reverse=True)
    while sorted_moves:
        move = sorted_moves.pop()
        path = _dfs(move.p, curr, dest, board, rlen, clen)
        if path is not None:
            return [curr] + path
    return None


def _create_move(point: Point, parent: Point, dest: Point,
                 board: List[List[int]]):
    # print(point)
    if point is None or point == parent or board[point.r][
            point.c] == BLOCKED_TILE:
        return None
    return Move(point, _long_term_cost(point, dest))


def _find_coords(board: List[List[int]], rlen: int,
                 clen: int) -> Tuple[Point, Point]:
    source_coords, target_coords = None, None
    ridx = 0
    while ridx < rlen and (source_coords is None or target_coords is None):
        cidx = 0
        while cidx < clen:
            bval = board[ridx][cidx]
            if bval == SOURCE_TILE:
                source_coords = Point(ridx, cidx)
            elif bval == TARGET_TILE:
                target_coords = Point(ridx, cidx)
            cidx += 1
        ridx += 1
    return (source_coords, target_coords)


# heuristic function: should never overestimate the distance to the goal
def _long_term_cost(curr: Point, dest: Point) -> float:
    return math.sqrt((dest.r - curr.r)**2 + (dest.c - curr.c)**2)


board1 = [[3, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 0], [0, 0, 0, 1, 0],
          [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [2, 0, 0, 0, 0]]
