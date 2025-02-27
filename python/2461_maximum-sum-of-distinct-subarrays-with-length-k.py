from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
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
            if uniq_m >= k:
                res = max(res, sum)
            tmp = nums[i - (k - 1)]
            sum -= tmp
            tmp_cnt = cnt[tmp]
            if tmp_cnt == 1:
                uniq_m -= 1
            cnt[tmp] = tmp_cnt - 1
        return res


s = Solution()
print(s.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15)
print(s.maximumSubarraySum([4, 4, 4], 3) == 0)
