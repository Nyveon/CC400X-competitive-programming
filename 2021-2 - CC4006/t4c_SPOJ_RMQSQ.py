# Eric
# Tarea 4 Ejercicio 3
# C - El más pequeño

import sys


class SegmentTree:
    """ Class for containing a segment tree and its behaviours, by Eric """

    def __init__(self, array, operation=lambda x, y: x + y):
        self.n = len(array)
        self.tree = [0] * (4 * self.n)
        self.operation = operation
        self.build(0, 0, self.n - 1, array)

    def build(self, index, left, right, array):
        """ Build a node recursively """

        if right - left == 0:
            self.tree[index] = array[left]
            return

        self.build(2 * index + 1, left, (left+right)//2, array)
        self.build(2 * index + 2, (left + right)//2 + 1, right, array)
        self.tree[index] = self.operation(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def _update(self, index, left, right, position, value):
        """ Internal recursive update function """

        if position > right or position < left:
            return

        if left == right:
            self.tree[index] = value
            return

        self._update(2 * index + 1, left, (left + right)//2, position, value)
        self._update(2 * index + 2, (left + right)//2 + 1, right, position, value)
        self.tree[index] = self.operation(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def update(self, index, value):
        """ Update a specific node """
        self._update(0, 0, self.n - 1, index, value)

    def _query(self, index, left, right, query_left, query_right):
        """ Internal recursive query """
        if left >= query_left and right <= query_right:
            return self.tree[index]

        mid = (left + right)//2

        if query_right <= mid:
            return self._query(2 * index + 1, left, mid, query_left, query_right)
        elif query_left > mid:
            return self._query(2 * index + 2, mid + 1, right, query_left, query_right)

        _left = self._query(2 * index + 1, left, mid, query_left, query_right)
        _right = self._query(2 * index + 2, mid + 1, right, query_left, query_right)
        return self.operation(_left, _right)

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)


# Input
n = int(sys.stdin.readline())
numbers = [int(x) for x in sys.stdin.readline().split()]
q = int(sys.stdin.readline())

# Processing
segtree = SegmentTree(numbers, lambda x, y: min(x, y))

# Queries
for i in range(q):
    qi, ji = [int(x) for x in sys.stdin.readline().split()]
    print(segtree.query(qi, ji))
