class GapBuffer:

    def __init__(self, gap_size: int = 16) -> None:
        self._gap_size = gap_size
        self._buffer = bytearray(self._gap_size)
        self._gap_start = 0
        self._gap_end = self._gap_size
        self._n = self._gap_size

    def cursor_left(self):
        if self._gap_start == 0:
            return
        self._gap_start -= 1
        self._gap_end -= 1
        self._buffer[self._gap_end] = self._buffer[self._gap_start]

    def cursor_right(self):
        if self._gap_end == self._n:
            return
        self._buffer[self._gap_start] = self._buffer[self._gap_end]
        self._gap_start += 1
        self._gap_end += 1

    def delete(self):
        if self._gap_start == 0:
            return
        self._gap_start -= 1

    def insert(self, char: int):
        if self._gap_start == self._gap_end:
            self._grow()
        self._buffer[self._gap_start] = char
        self._gap_start += 1

    def _grow(self):
        self._buffer.extend(bytearray(self._gap_size))
        src_start, src_end = self._gap_end, self._gap_end
        dst_start, dst_end = src_start + self._gap_size, src_end + self._gap_size
        self._buffer[dst_start:dst_end] = self._buffer[src_start:src_end]
        self._n += self._gap_size

    def prettyprint(self) -> str:
        return self._buffer[:self._gap_start].decode(
        ) + self._buffer[self._gap_end:].decode()

    def __repr__(self) -> str:
        return f"GapBuffer(gap_size: {self._gap_size}, gap_start: {self._gap_start}, gap_end: {self._gap_end}, n: {self._n})"


if __name__ == "__main__":
    gb = GapBuffer()
    gb.insert(ord('r'))
    gb.cursor_left()
    gb.insert(ord('e'))
    gb.cursor_right()
    gb.insert(ord('y'))
    print(gb.prettyprint())
    gb.delete()
    print(gb.prettyprint())
