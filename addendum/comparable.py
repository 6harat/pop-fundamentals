class Comparable(object):
    def __init__(self, val):
        self.val = val
    def __eq__(self, that):
        if not isinstance(that, Comparable):
            return NotImplemented
        return self.val == that.val
    def __ne__(self, that):
        if not isinstance(that, Comparable):
            return NotImplemented
        return self.val != that.val
    def __lt__(self, that):
        if not isinstance(that, Comparable):
            return NotImplemented
        return self.val < that.val
    def __gt__(self, that):
        if not isinstance(that, Comparable):
            return NotImplemented
        return self.val > that.val
    def __le__(self, that):
        if not isinstance(that, Comparable):
            return NotImplemented
        return self.__lt__(that) or self.__eq__(that)
    def __ge__(self, that):
        if not isinstance(that, Comparable):
            return NotImplemented
        return self.__gt__(that) or self.__eq__(that)

    def __repr__(self):
        return 'Comparable(val={})'.format(self.val)