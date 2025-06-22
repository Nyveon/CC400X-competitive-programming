from collections import Counter

# O(N + A^2) where A is number of different possible characters
# So, O(N)-ish


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = Counter(word)
        least_changes = len(word)

        # Candidate: the potential least counted character of the result
        for candidate_character in counts:
            changes = 0
            candidate_count = counts[candidate_character]
            print(f"{candidate_character} : {candidate_count}")

            for other_character in counts:
                other_count = counts[other_character]

                if other_count < candidate_count:
                    changes += other_count
                elif other_count > candidate_count + k:
                    changes += other_count - candidate_count - k

            if changes < least_changes:
                least_changes = changes

        return least_changes
