from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        s = [0] * (n + 1)
        cnt = defaultdict(int)
        cnt[0] = 1

        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
            res += cnt[s[i + 1] - k]
            cnt[s[i + 1]] += 1
        return res


    # wrong code
    # cnt[0] = 1
    # for i in range(n):
    #     s[i + 1] = nums[i] + s[i]
    #     cnt[s[i + 1]] += 1
    #
    # for j in range(n + 1):
    #     print(f'j={j},s[j]={s[j]},cnt[s[j]-k]={cnt[s[j] - k]}')
    #     res += cnt[s[j] - k]
    #
    # return res

    # V2: two loops
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     res = 0
    #     n = len(nums)
    #     s = [0] * (n + 1)
    #     cnt = defaultdict(int)
    #     cnt[s[0]] = 1
    #     for i in range(n):
    #         s[i + 1] = nums[i] + s[i]
    #         cnt[s[i + 1]] += 1
    #
    #     for j in range(n, 0, -1):
    #         cnt[s[j]] -= 1  # 先减去自己
    #         res += cnt[s[j] - k]
    #
    #     return res

    # Time Limit Exceeded
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     res = 0
    #     n = len(nums)
    #     s = [0] * (n + 1)
    #     i = 0
    #     for j in range(i + 1, n + 1):
    #         s[j] = nums[j - 1] + s[j - 1]
    #         if s[j] == k:
    #             res += 1
    #     for i in range(1, n):
    #         for j in range(i + 1, n + 1):
    #             s[j] = s[j] - nums[i - 1]
    #             if s[j] == k:
    #                 res += 1
    #     return res


s = Solution()
# print(s.subarraySum([1, 1, 1], 2) == 2)
# print(s.subarraySum([1, 2, 3], 3) == 2)
print(s.subarraySum([1, 1, -1, 1, -1], 1) == 6)
