from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        cnt1 = sum(nums)
        if cnt1 == 0:
            return 0
        res = n
        cnt0 = 0
        for i in range(-(cnt1 - 1), n):
            if nums[i] == 0:
                cnt0 += 1
            if i < 0:
                continue
            res = min(res, cnt0)
            if nums[(i - (cnt1 - 1)) % n] == 0:
                cnt0 -= 1
        return res


s = Solution()
print(s.minSwaps([0, 1, 0, 1, 1, 0, 0]) == 1)
print(s.minSwaps([1, 1, 0, 0, 1]) == 0)
print(s.minSwaps([0, 0, 0]) == 0)
