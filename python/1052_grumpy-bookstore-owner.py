from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sum_g_max = sum_g_window = sum_happy = 0

        for i in range(len(customers)):
            if grumpy[i]:
                sum_g_window += customers[i]
            else:
                sum_happy += customers[i]
            if i < minutes - 1:
                continue
            sum_g_max = max(sum_g_max, sum_g_window)
            if grumpy[i - (minutes - 1)]:
                sum_g_window -= customers[i - (minutes - 1)]
        return sum_happy + sum_g_max


s = Solution()
print(s.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) == 16)
