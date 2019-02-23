class BinaryNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # add null checks for `that` node in all the comparisons below and reduce __ne__ as not of __eq__
    def __eq__(self, that):
        return self.data == that.data
    def __ne__(self, that):
        return self.data != that.data
    def __lt__(self, that):
        return self.data < that.data
    def __gt__(self, that):
        return self.data > that.data
    def __le__(self, that):
        return self.__lt__(that) or self.__eq__(that)
    def __ge__(self, that):
        return self.__gt__(that) or self.__eq__(that)
        
    def __repr__(self):
        return 'BinaryNode(data={data}, left={left}, right={right})'.format(
            data=self.data,
            left=self.left.data if self.left else None,
            right=self.right.data if self.right else None
        )