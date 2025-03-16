import collections
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)
        res = -1
        if target < 0:
            return res
        if target == 0:
            return n

        left = s = 0
        for right in range(n):
            s += nums[right]
            while s >= target:
                if s == target:
                    res = max(res, right - left + 1)
                s -= nums[left]
                left += 1
        return res if res == -1 else n - res

    # def minOperations(self, nums: List[int], x: int) -> int:
    #     n = len(nums)
    #     res = n + 1
    #     suffix = [0] * n
    #     suffix_dict = collections.defaultdict(int)
    #     s = 0
    #     suffix_dict[0] = -1
    #     for j in range(n - 1, -1, -1):
    #         s += nums[j]
    #         sj = n - 1 - j
    #         suffix[sj] = s
    #         suffix_dict[s] = sj
    #     s = 0
    #     for i in range(-1, n):
    #         if i >= 0:
    #             s += nums[i]
    #         if x - s in suffix_dict:
    #             res = min(res, suffix_dict[x - s] + i + 2)
    #     return -1 if res == n + 1 else res


s = Solution()
print(s.minOperations([1, 1, 4, 2, 3], 5) == 2)
print(s.minOperations([5, 6, 7, 8, 9], 4) == -1)
print(s.minOperations([3, 2, 20, 1, 1, 3], 10) == 5)
print(s.minOperations([8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309],
                      134365))
