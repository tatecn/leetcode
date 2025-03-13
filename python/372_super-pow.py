from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        m = 1337
        for i in range(len(b) - 1, -1, -1):
            res = (res * pow(a, b[i], m)) % m
            a = pow(a, 10, m)
        return res
