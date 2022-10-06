# Eric K.
# Meta Global Hackathon 2022
# Looks like segment tree

from decimal import *
getcontext().prec = 20

class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def multiply(self, start, stop, value):
        """lazily multiply value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] *= value
                self.data[start] *= value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] *= value
                self.data[stop] *= value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)


    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)


# What range?
def get_level(x):
    if x < 10**6:
        return 0
    elif x < 2*10**6:
        return 1
    else:
        return 2

def output_format(x):
    #val = round(x, 6) # Future eric: maybe not round
    #return '{:.6f}'.format(val)
    return str(x)

# Input
lines = []
file_name = "test_input.txt"
#file_name = ".txt"
with open(file_name, "r") as f:
    for line in f:
        lines.append(line.rstrip())

# Processing
test_cases = int(lines[0])
lines = lines[1:]

for t in range(test_cases):
    # Number of employees and number of queries
    n, q = map(int, lines[0].split())

    # Starting wages
    wages = list(map(int, lines[1].split()))
    # convert all to decimal
    wages = [Decimal(x) for x in wages]

    # Make segment tree
    st = LazySegmentTree(wages, 0, lambda x, y: Decimal(x) + Decimal(y))

    # Queries
    for i in range(q):
        query = [int(x) for x in lines[i + 2].split()]
        print(query)
        if query[0] == 1: # Update tree
            percentages = [query[1], query[2], query[3]]
            # convert to decimal
            percentages = [Decimal(x) for x in percentages]
            e = query[4] - 1 # Employee ID
            r = query[5] # Number of times the query happens
            for _ in range(r):
                for j in range(0, n):
                    current_value = Decimal(st.query(j, j + 1))
                    level = get_level(current_value)
                    st.add(j, j + 1, Decimal(current_value) * Decimal(percentages[level]) / Decimal(100))
                print(output_format(st.query(e, e + 1)))
        elif query[0] == 2: # Query tree
            e1 = query[1] - 1
            e2 = query[2] - 1
            ans = st.query(e1, e2 + 1)
            print(output_format(ans))
        print("==============")

    # Remove first bit of lines
    lines = lines[2 + q:]



# Output
ans = ''
with open("out.txt", "w") as f:
    f.write(ans)
