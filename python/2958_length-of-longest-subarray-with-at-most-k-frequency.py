import collections
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = res = 0
        cnt = collections.defaultdict(int)
        for i in range(len(nums)):
            cnt[nums[i]] += 1
            while cnt[nums[i]] > k:
                cnt[nums[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
        return res


s = Solution()
print(s.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) == 6)
print(s.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) == 2)
print(s.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) == 4)
