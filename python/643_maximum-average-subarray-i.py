from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')
        sum = 0
        n = len(nums)
        l = r = 0
        while r < n:
            sum += nums[r]
            if r - l + 1 == k:
                res = max(sum, res)
                sum -= nums[l]
                l += 1
            r += 1
        return res / k

    # wrong code for [-1], 1
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    #     res = 0
    #     sum = 0
    #     n = len(nums)
    #     l = r = 0
    #     while r < n:
    #         sum += nums[r]
    #         if r - l + 1 == k:
    #             res = max(sum, res)
    #             sum -= nums[l]
    #             l += 1
    #         r += 1
    #     return res / k


s = Solution()
print(s.findMaxAverage([-1], 1))
