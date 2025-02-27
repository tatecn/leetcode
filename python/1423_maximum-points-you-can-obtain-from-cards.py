import operator
from typing import List
import itertools


class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        a, b = itertools.tee(itertools.accumulate(cardPoints, initial=0))
        b = itertools.islice(b, len(cardPoints) - k, None)
        return sum(cardPoints) - min(itertools.starmap(operator.sub, zip(b, a)))

    # def maxScore(self, cardPoints: List[int], k: int) -> int:
    #     n = len(cardPoints)
    #     m = n - k
    #     sum_all = res = min_s = sum(cardPoints[:m])
    #     for i in range(m, n):
    #         sum_all += cardPoints[i]
    #         min_s += cardPoints[i] - cardPoints[i - m]
    #         res = min(res, min_s)
    #     return sum_all - res

    # def maxScore(self, cardPoints: List[int], k: int) -> int:
    #     res = max_s = sum(cardPoints[:k])
    #     for i in range(1, k + 1):
    #         max_s += cardPoints[-i] - cardPoints[k - i]
    #         res = max(res, max_s)
    #     return res

    # My version
    # def maxScore(self, cardPoints: List[int], k: int) -> int:
    #     n = len(cardPoints)
    #     if k == 1:
    #         return max(cardPoints[0], cardPoints[-1])
    #     elif k == n:
    #         sum = 0
    #         for num in cardPoints:
    #             sum += num
    #         return sum
    #
    #     res = sum = 0
    #     for i in range(n - k, n + k):
    #         num = cardPoints[i] if i < n else cardPoints[i - n]
    #         sum += num
    #         if i < n - 1:
    #             continue
    #         res = max(res, sum)
    #         if i < n + k - 1:
    #             tmp = cardPoints[(n - k) + i - (n - 1)]
    #             sum -= tmp
    #     return res


s = Solution()
print(s.maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12)
print(s.maxScore([2, 2, 2], 2) == 4)
print(s.maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55)
