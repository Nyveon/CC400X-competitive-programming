from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # - Only one valid answer exists
        # - Can't use the same element twice
        # Goal: less than O(n^2)

        values_indices = defaultdict(int)

        for index, number in enumerate(nums): # O(n)
            complement = target - number
            if complement in values_indices:  # O(1) avg
                return [index, values_indices[complement]]
            values_indices[number] = index # O(1) avg
        
        # Should never reach here since there's always one solution
