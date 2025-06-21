class SolutionA:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefixes = []
        cumulative = 1

        for num in nums:  # O(n)
            prefixes.append(cumulative)
            cumulative *= num

        suffixes = []
        cumulative = 1
        for num in reversed(nums):  # O(n)
            suffixes.append(cumulative)
            cumulative *= num

        answer = []
        for i in range(len(nums)):  # O(n)
            answer.append(prefixes[i] * suffixes[-i - 1])

        return answer


# Alternative answer with only 2 fors


class SolutionB:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        cumulative = 1

        for num in nums:  # O(n)
            answer.append(cumulative)
            cumulative *= num

        cumulative = 1
        for i, num in enumerate(reversed(nums)):  # O(n)
            answer[-i - 1] *= cumulative
            cumulative *= num

        return answer
