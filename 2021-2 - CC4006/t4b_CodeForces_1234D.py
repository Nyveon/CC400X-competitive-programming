# Eric
# Tarea 4 Ejercicio 2
# B - Letras distintas

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

        if left == right:
            self.tree[index] = array[left]
            return

        self.build(2 * index + 1, left, (left + right)//2, array)
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
s = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline())


def letter_bitmask(c):
    """ Converts an ASCII lowercase letter to a single bit at the corresponidng position """
    return 2**(ord(c) - 97)


def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


array = []
for character in s:
    array.append(letter_bitmask(character))


"""
     7
  3     5
 a  b  a  c
[1, 2, 1, 4]

     15
  3     12   
 a  b  d  c
[1, 2, 8, 4]
"""


segtree = SegmentTree(array, lambda x, y: x | y)


for i in range(q):
    qt, qi, ji = sys.stdin.readline().rstrip().split()

    if qt == "1":
        segtree.update(int(qi) - 1, letter_bitmask(ji))
    else:
        print(count_set_bits(segtree.query(int(qi) - 1, int(ji) - 1)))
