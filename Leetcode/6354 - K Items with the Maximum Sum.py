# Eric K
# Weekly Contest 338
# AC

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int,
                             numNegOnes: int, k: int) -> int:
        total = 0
        remaining = k

        if numOnes < remaining:
            total += numOnes
            remaining -= numOnes
        else:
            return k

        if numZeros < remaining:
            remaining -= numZeros
        else:
            return total

        total -= remaining
        return total
