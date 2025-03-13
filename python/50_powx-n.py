import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if math.isclose(x, 0, rel_tol=1e-9, abs_tol=0.0):
            return 1 if n == 0 else 0
        if n < 0:
            n = abs(n)
            x = 1 / x
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


s = Solution()
print(s.myPow(0, -2))
print(s.myPow(0, 0))
