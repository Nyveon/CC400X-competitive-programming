from collections import Counter

# Idea: descending frequency adjustment wave (since we can only subtract)
#   If same frequency is found, subtract the second one then move on
#   If a greater frequency is found, subtract until same - 1
# Time Complexity:
#   Counting: O(n)
#   Sorting: O(n log n)
#   Greedy: O(n)
#   Total O(n log n)
# Space Complexity:
# + O(A) for counter where A is number of possible characters


class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s).most_common()  # Sorted descending
        last_count = 1000000
        changes = 0

        for character, count in counts:
            print(character, count, last_count)
            if count >= last_count:
                delta = 1 + count - last_count
                count -= delta
                changes += delta
            last_count = max(1, count)  # Ignore negatives

        return changes
