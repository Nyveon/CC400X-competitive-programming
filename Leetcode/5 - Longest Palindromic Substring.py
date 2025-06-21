class Solution:
    def still_valid(self, s: str, left_pointer: int, right_pointer: int) -> bool:
        if left_pointer < 0 or right_pointer >= len(s):
            return False

        if s[left_pointer] != s[right_pointer]:
            return False

        return True

    def propagate_palindrome(
        self, s: str, left_pointer: int, right_pointer: int
    ) -> int:
        current_run_length = right_pointer - left_pointer - 1

        while self.still_valid(s, left_pointer, right_pointer):
            current_run_length += 2
            left_pointer -= 1
            right_pointer += 1

        return (current_run_length, left_pointer)

    def longestPalindrome(self, s: str) -> str:
        longest_run_length = 0
        longest_run_start = 1

        for index in range(len(s)):
            run_length, left = self.propagate_palindrome(
                s, index - 1, index + 1
            )  # Odd palindromes
            if run_length > longest_run_length:
                longest_run_length = run_length
                longest_run_start = left + 1

            run_length, left = self.propagate_palindrome(
                s, index, index + 1
            )  # Even palindromes
            if run_length > longest_run_length:
                longest_run_length = run_length
                longest_run_start = left + 1

        return s[longest_run_start : longest_run_start + longest_run_length]
