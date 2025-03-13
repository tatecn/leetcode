from typing import List


class Solution:

    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [nums[(i + c) % n] for i, c in enumerate(nums)]

    # My version to avoid index out of range
    # def constructTransformedArray(self, nums: List[int]) -> List[int]:
    #     res = list(nums)
    #     n = len(nums)
    #     for i in range(n):
    #         dest = (i + nums[i] + n) % n if nums[i] < 0 else (nums[i] + i) % n
    #         res[i] = nums[dest]
    #     return res


s = Solution()
print(s.constructTransformedArray([3, -2, 1, 1]) == [1, 1, 1, 3])
print(s.constructTransformedArray([-1, 4, -1]) == [-1, -1, 4])
