from collections import defaultdict
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res = 0
        cnt = defaultdict(int)
        uniq_m = sum = 0
        for i, num in enumerate(nums):
            sum += num
            existed = cnt[num]
            if existed == 0:
                uniq_m += 1
            cnt[num] = existed + 1

            if i < k - 1:
                continue
            if uniq_m >= m:
                res = max(res, sum)
            tmp = nums[i - (k - 1)]
            sum -= tmp
            tmp_cnt = cnt[tmp]
            if tmp_cnt == 1:
                uniq_m -= 1
            cnt[tmp] = tmp_cnt - 1
        return res


s = Solution()
print(s.maxSum([2, 6, 7, 3, 1, 7], 3, 4) == 18)
print(s.maxSum([5, 9, 9, 2, 4, 5, 4], 1, 3) == 23)
print(s.maxSum([1, 2, 1, 2, 1, 2, 1], 3, 3) == 0)
