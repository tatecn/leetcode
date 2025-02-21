from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = sum = 0
        sum_t = k * threshold
        for r, x in enumerate(arr):
            sum += x
            if r < k - 1:
                continue
            if sum >= sum_t:
                res += 1
            sum -= arr[r + 1 - k]
        return res
