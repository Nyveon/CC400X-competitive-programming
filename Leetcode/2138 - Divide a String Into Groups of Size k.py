import math

# Code could be much simpler/more consie using slicing
# Time: O(n)
# Aux space: O(n)

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        original_length = len(s)
        final_length = math.ceil(original_length / k) * k

        current = ""
        output = []
        for i in range(final_length):
            if i < original_length:
                current += s[i]
            else:
                current += fill

            if i % k == k - 1:
                output.append(current)
                current = ""  
            
        return output
