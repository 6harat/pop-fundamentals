class BinaryHeap(object):
    def __init__(self, vals=None, is_max=False):
        self._is_max = is_max
        self._vals = vals[:] if vals else []
        self._size = len(self._vals)
        self._heapify()
    
    def _swap(self, i, j):
        temp = self._vals[i]
        self._vals[i] = self._vals[j]
        self._vals[j] = temp

    def _parent_node_idx(self, idx):
        p_idx = (idx - 1) / 2
        return None if p_idx < 0 else p_idx

    def _left_node_idx(self, idx):
        l_idx = idx * 2 + 1
        return None if l_idx >= self._size else l_idx

    def _right_node_idx(self, idx):
        r_idx = idx * 2 + 2
        return None if r_idx >= self._size else r_idx

    def _heapify(self):
        for i in range(self._size-1, -1, -1):
            self._heapifyDown(idx=i)

    def _is_in_order(self, parent, child):
        if self._is_max:
            return self._vals[parent] >= self._vals[child]
        else:
            return self._vals[parent] <= self._vals[child]

    def _heapifyUp(self):
        if not self._vals:
            return
        idx = self._size - 1
        p_idx = self._parent_node_idx(idx)
        while p_idx >= 0 and not self._is_in_order(p_idx, idx):
            self._swap(idx, p_idx)
            idx = p_idx
            p_idx = self._parent_node_idx(idx)

    def _heapifyDown(self, idx=0):
        if not self._vals:
            return
        while True:
            l_idx = self._left_node_idx(idx)
            if l_idx is None:
                return
            r_idx = self._right_node_idx(idx)

            selected_idx = idx
            if not self._is_in_order(selected_idx, l_idx):
                selected_idx = l_idx
            if r_idx and not self._is_in_order(selected_idx, r_idx):
                selected_idx = r_idx
            
            if selected_idx == idx:
                return

            self._swap(idx, selected_idx)
            idx = selected_idx
        return

    def is_empty(self):
        return self._size == 0

    def push(self, val):
        self._vals.append(val)
        self._size += 1
        self._heapifyUp()
    
    def pop(self):
        if not self._vals:
            return None
        if self._size == 1:
            self._size -= 1
            return self._vals.pop()
        el = self._vals[0]
        self._vals[0] = self._vals.pop()
        self._size -= 1
        self._heapifyDown()
        return el

    def peek(self):
        return None if not self._vals else self._vals[0]