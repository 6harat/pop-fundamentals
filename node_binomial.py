class BinomialNode(object):
    def __init__(self, data, parent=None, degree=0, child=None, sibling=None):
        self.data = data
        self.parent = parent
        self.degree = degree
        self.child = child
        self.sibling = sibling

    def __repr__(self):
        return 'BinomialNode(data={data}, parent={parent}, degree={degree}, child={child}, sibling={sibling})'.format(
            data=self.data,
            parent=self.parent.data if self.parent else None,
            degee=self.degree,
            child=self.child.data if self.child else None,
            sibling=self.sibling.data if self.sibling else None
        )