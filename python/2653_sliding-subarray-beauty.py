import bisect
from typing import List


class Solution:

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = [0] * (n - k + 1)
        cnt = [0] * 101
        for i in range(k - 1):
            cnt[nums[i]] += 1
        for i in range(k - 1, n):
            cnt[nums[i]] += 1
            left = x
            pre = i - (k - 1)
            for j in range(-50, 0):
                left -= cnt[j]
                if left <= 0:
                    res[pre] = j
                    break
            cnt[nums[pre]] -= 1
        return res

    # def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
    #     n = len(nums)
    #     m = n - k + 1
    #     res = [0] * m
    #     listk = sorted(nums[:k - 1])
    #
    #     for i in range(k - 1, n):
    #         bisect.insort_right(listk, nums[i])
    #         pre = i - (k - 1)
    #         res[pre] = listk[x - 1] if listk[x - 1] < 0 else 0
    #         listk.pop(bisect.bisect_left(listk, nums[pre]))
    #     return res


s = Solution()
print(s.getSubarrayBeauty([1, -1, -3, -2, 3], 3, 2) == [-1, -2, -2])
print(s.getSubarrayBeauty([-1, -2, -3, -4, -5], 2, 2) == [-1, -2, -3, -4])
print(s.getSubarrayBeauty([-3, 1, 2, -3, 0, -3], 2, 1) == [-3, 0, -3, -3, -3])
