from typing import List


class Solution:

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        sum = 0
        dest_i = 2 * k
        step = dest_i + 1
        for r in range(n):
            sum += nums[r]
            if r < dest_i:
                continue
            res[r - k] = sum // step
            sum -= nums[r - dest_i]
        return res

    # V1: my version
    # def getAverages(self, nums: List[int], k: int) -> List[int]:
    #     n = len(nums)
    #     res = [-1] * n
    #     sum = l = i = 0
    #     step = 2 * k + 1
    #     for r in range(n):
    #         sum += nums[r]
    #         if i < k:
    #             i += 1
    #         if i - k >= l and i + k <= r and r - l + 1 == step:
    #             res[i] = sum // step
    #             i += 1
    #             sum -= nums[l]
    #             l += 1
    #     return res


s = Solution()
# print(s.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
print(s.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3) == [-1, -1, -1, 5, 4, 4, -1, -1, -1])
