from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        res = l1 = l2 = s1 = s2 = 0

        for r in range(n):
            s1 += nums[r]
            s2 += nums[r]

            while l1 <= r and s1 >= goal:
                s1 -= nums[l1]
                l1 += 1
            while l2 <= r and s2 >= goal + 1:
                s2 -= nums[l2]
                l2 += 1
            res += (l1 - l2)

        return res

    # V1: same code with 560
    # def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    #     res = 0
    #     n = len(nums)
    #     s = [0] * (n + 1)
    #     cnt = defaultdict(int)
    #     cnt[0] = 1
    #
    #     for i, x in enumerate(nums):
    #         s[i + 1] = s[i] + x
    #         res += cnt[s[i + 1] - goal]
    #         cnt[s[i + 1]] += 1
    #
    #     return res


s = Solution()
# print(s.numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4)
# print(s.numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15)
print(s.numSubarraysWithSum([1, 0, 1, 0, 0, 1, 0], 2))
