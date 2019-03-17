class BinaryNode(object):
    def __init__(self, key, left=None, right=None, record=None, height=None):
        self.key = key
        self.record = record
        self.left = left
        self.right = right
        self.height = height

    def __eq__(self, that):
        return bool(that) and self.key == that.key
    def __ne__(self, that):
        return self.__eq__(that)
    def __lt__(self, that):
        return bool(that) and self.key < that.key
    def __gt__(self, that):
        return bool(that) and self.key > that.key
    def __le__(self, that):
        return self.__lt__(that) or self.__eq__(that)
    def __ge__(self, that):
        return self.__gt__(that) or self.__eq__(that)
        
    def __repr__(self):
        return 'BinaryNode(key={key}, left={left}, right={right}, height={height})'.format(
            key=self.key,
            left=self.left.key if self.left else None,
            right=self.right.key if self.right else None,
            height=self.height
        )

class BinomialNode(object):
    def __init__(self, key, parent=None, degree=0, child=None, sibling=None, record=None):
        self.key = key
        self.record = record
        self.parent = parent
        self.degree = degree
        self.child = child
        self.sibling = sibling

    def __repr__(self):
        return 'BinomialNode(key={key}, parent={parent}, degree={degree}, child={child}, sibling={sibling})'.format(
            key=self.key,
            parent=self.parent.key if self.parent else None,
            degee=self.degree,
            child=self.child.key if self.child else None,
            sibling=self.sibling.key if self.sibling else None
        )

class Entry(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
    def __repr__(self):
        return 'Entry(key={key}, value={value}'.format(
            key=self.key,
            value=self.value
        )

class LinkedEntry(object):
    def __init__(self, key, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next
    def __repr__(self):
        return 'LinkedEntry(key={key}, value={value}, next={next}'.format(
            key=self.key,
            value=self.value,
            next=self.next.key if self.next else None
        )

class MultiwayNode(object):
    def __init__(self, entries, degree=3, children=None, is_leaf=False):
        self.degree = degree
        self.entries = entries
        self._num_entry = self._len(self.entries)
        self.children = children
        self._num_child = self._len(self.children)
        self.is_leaf = is_leaf
        self._validate()

    def _len(self, vals):
        return 0 if vals is None else len(vals)

    def _validate(self):
        if self._num_entry + 1 > self.degree:
            raise ValueError('num_entry {} for a node of {} degree can be at most {}'.format(
                self._num_entry,
                self.degree,
                self.degree-1 
            ))
        if self._num_child > self.degree:
            raise ValueError('num_child {} for a node of {} degree can be at most {}'.format(
                self._num_child,
                self.degree,
                self.degree
            ))
        if self.is_leaf and self._num_child > 0:
            raise ValueError('a leaf node can have no children')

