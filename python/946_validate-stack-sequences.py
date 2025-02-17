from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, j = [], 0
        for val in pushed:
            stack.append(val)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack


s = Solution()
print(s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
