from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        def get(i: int) -> int:
            if i == 0:
                return startTime[0]
            if i == n:
                return eventTime - endTime[i - 1]
            return startTime[i] - endTime[i - 1]

        n = len(startTime)
        k = k + 1
        res = sum_k = 0
        for i in range(n + 1):
            sum_k += get(i)
            if i < k - 1:
                continue
            res = max(res, sum_k)
            sum_k -= get(i - (k - 1))
        return res

    # def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
    #     n = len(startTime)
    #     free_time = [0] * (n + 1)
    #     free_time[0] = startTime[0]
    #     for i in range(1, n):
    #         free_time[i] = startTime[i] - endTime[i - 1]
    #     free_time[n] = eventTime - endTime[n - 1]
    #
    #     k = k + 1
    #     res = sum_k = 0
    #     for i in range(n + 1):
    #         sum_k += free_time[i]
    #         if i < k - 1:
    #             continue
    #         res = max(res, sum_k)
    #         sum_k -= free_time[i - (k - 1)]
    #     return res


s = Solution()
k = 1
print(s.maxFreeTime(5, k, [1, 3], [2, 5]) == 2)
print(s.maxFreeTime(10, k, [0, 2, 9], [1, 4, 10]) == 6)
print(s.maxFreeTime(5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]) == 0)
