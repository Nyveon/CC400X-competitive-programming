class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        final = []
        negatives = []

        for value in nums:
            squared = value**2

            if value < 0:
                negatives.append(squared)
                continue

            while negatives and negatives[-1] <= squared:
                final.append(negatives.pop())

            final.append(squared)

        while negatives:
            final.append(negatives.pop())

        return final
