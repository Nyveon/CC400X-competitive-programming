class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        number_set = set(nums)  # O(n)
        longest_run = 1

        # iterate over number_set instead of nums to prevent duplicate checks
        for number in number_set:
            ante = number - 1
            # potential optimization: also go backwards?
            if ante not in number_set:  # It's a run start
                # optimization: we can discard fast
                if (number + longest_run) not in number_set:
                    continue

                succ = number + 1
                run_length = 1

                while succ in number_set:
                    run_length += 1
                    succ += 1
                if run_length > longest_run:
                    longest_run = run_length

        return longest_run
