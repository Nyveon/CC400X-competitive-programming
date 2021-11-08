# Eric
# Tarea 4 Ejercicio 1
# A - Ataque estratégico

import sys
import array

class SegmentTree:
    """
    Class for containing a segment tree and its behaviours, by Eric
    Iterative version because performance
    Following GeekforGeeks guide
    """

    def __init__(self, _array, operation=lambda x, y: x + y):
        self.n = len(_array)
        self.tree = array.array('i', (0,)*(self.n*2))
        self.operation = operation

        for _i in range(self.n):
            self.tree[self.n + _i] = _array[_i]

        for _i in range(self.n - 1, 0, -1):
            self.tree[_i] = self.operation(self.tree[_i << 1], self.tree[_i << 1 | 1])

    def update(self, index, value):
        """ Update a specific node """
        self.tree[index + self.n] += value  # Only += for this solution
        index += self.n

        while index > 1:
            self.tree[index >> 1] = self.operation(self.tree[index], self.tree[index ^ 1])
            index >>= 1

    def query(self, left, right):
        """ Iterative query """
        left += self.n
        right += self.n
        ans = 0
        while left < right:
            if left & 1:
                ans += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                ans += self.tree[right]
            left >>= 1
            right >>= 1
        return ans




# Input
n = int(sys.stdin.readline())
a = (int(x) for x in sys.stdin.readline().split())

# Compressing the input
a_indexed = list(enumerate(a))
a_indexed.sort(key=lambda x: x[1])  # O(10^6 log 10^6) = 6*10^6 | 5 seconds -> about 5*10^8 TLE, we gucci

# Allocating memory
a_compressed = array.array('i', (0,)*n)  # 10^6 ?
right_frequencies = array.array('i', (0,)*1000001)
left_frequencies = array.array('i', (0,)*1000001)


uniques = 0
previous = -1
for i in range(n):  # 10^6
    index, current = a_indexed[i]

    if current != previous:
        uniques += 1
        previous = current
    a_compressed[index] = uniques
    right_frequencies[uniques] += 1

uniques += 1

# Process

# Segment tree
right_segtree = SegmentTree(right_frequencies, lambda x, y: x + y)
left_segtree = SegmentTree(left_frequencies, lambda x, y: x + y)

# Queries and updates
ans = 0
for i in range(n):  # 10^6
    current = a_compressed[i]

    right_segtree.update(current, -1)

    # Query
    ans_L = left_segtree.query(current, uniques)
    ans_R = right_segtree.query(0, current)
    #print(ans_L, ans_R, current-1)
    ans += ans_L * ans_R

    # Update
    left_segtree.update(current, 1)
    #right_segtree.update(current, -1)

sys.stdout.write(str(ans) + "\n")