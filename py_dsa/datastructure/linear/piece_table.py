from dataclasses import dataclass
from typing import List

ORIGINAL: str = "original"
DELTA: str = "delta"


@dataclass
class Piece:
    source: str
    start_idx: int
    length: int


@dataclass
class PieceTable:
    original_text: str

    def __post_init__(self):
        self._delta_text: str = ""
        self._delta_length: int = 0
        self._original_length: int = len(self.original_text)
        self._pieces: List[Piece] = []
        self._pieces_length = 0
        if self._original_length > 0:
            self._pieces.append(Piece(ORIGINAL, 0, self._original_length))
            self._pieces_length += 1

    def insert(self, index: int, text: str):
        text_length = len(text)
        dpiece = Piece(DELTA, self._delta_length, text_length)
        self._delta_text += text
        self._delta_length += text_length

        pidx, tidx = 0, 0
        while tidx < index and pidx < self._pieces_length:
            tidx += self._pieces[pidx].length
            pidx += 1

        if tidx == index:
            self._pieces.insert(pidx, dpiece)
            self._pieces_length += 1
            return

        cpiece = self._pieces[pidx - 1]
        clip_length = tidx - index
        lpiece = Piece(cpiece.source, cpiece.start_idx,
                       cpiece.length - clip_length)
        rpiece = Piece(cpiece.source,
                       cpiece.start_idx + cpiece.length - clip_length,
                       clip_length)
        self._pieces[pidx - 1] = lpiece
        self._pieces.insert(pidx, rpiece)
        self._pieces.insert(pidx, dpiece)
        self._pieces_length += 2

    def delete(self, index: int, length: int):
        pidx, tidx = 0, 0
        while tidx < index and pidx < self._pieces_length:
            pass

    def prettyprint(self):
        result = ""
        for piece in self._pieces:
            sidx, eidx = piece.start_idx, piece.start_idx + piece.length
            if piece.source == ORIGINAL:
                result += self.original_text[sidx:eidx]
            else:
                result += self._delta_text[sidx:eidx]
        return result
