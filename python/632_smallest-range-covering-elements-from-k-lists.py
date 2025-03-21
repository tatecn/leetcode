from typing import List
from math import inf
import collections


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pairs = sorted([(num, i) for i, arr in enumerate(nums) for num in arr])
        res_l, res_r = 0, inf
        k = len(nums)
        cnt = [0] * k
        non_empty = left = 0
        for num_r, i in pairs:
            if cnt[i] == 0:
                non_empty += 1
            cnt[i] += 1
            while non_empty == k:
                num_l, j = pairs[left][0], pairs[left][1]
                if num_r - num_l < res_r - res_l:
                    res_r, res_l = num_r, num_l
                if cnt[j] == 1:
                    non_empty -= 1
                cnt[j] -= 1
                left += 1

        return [res_l, res_r]


s = Solution()
print(s.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]) == [20, 24])
print(s.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == [1, 1])
