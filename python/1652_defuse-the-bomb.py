from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        if k > 0:
            step = k
            right = step + 1
        else:
            step = -k
            right = n
        sum_k = sum(code[right - step:right])
        for i in range(n):
            res[i] = sum_k
            sum_k += code[right % n] - code[(right - step) % n]
            right += 1
        return res


s = Solution()
# print(s.decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13])
print(s.decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13])
