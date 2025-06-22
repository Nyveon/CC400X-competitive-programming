from collections import Counter

# Idea 1:
# O(n2), but n is small so its ok
# Counter of letters
# Counter of counts of letters
# Went with this one because easier to program

# Idea 2:
# Same as before but iterate unique characters instead of entire word
# O(n * A) where A is number of unique characters

# Idea 3: Similar to leetcode 1647
# Sort counter descending
# Iterate left to right once, seeing if decreasing each would:
# - leave it in a separate class
# - move it to an already existing class
# - make it 0
# maybe some other edge cases
# O(n log n)


class Solution:
    def equalFrequency(self, word: str) -> bool:
        unique_characters = set(word)

        for character in unique_characters:
            counts = Counter(word)
            counts[character] -= 1
            if counts[character] == 0:
                del counts[character]

            counts_counter = Counter(counts.values())
            if len(counts_counter) <= 1:
                return True

        return False


class Solution1:
    def equalFrequency(self, word: str) -> bool:
        for character in word:
            counts = Counter(word)
            counts[character] -= 1
            if counts[character] == 0:
                del counts[character]

            counts_counter = Counter(counts.values())
            if len(counts_counter) <= 1:
                return True

        return False
