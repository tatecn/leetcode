class Solution:
    def monkeyMove(self, n: int) -> int:
        m = pow(10, 9) + 7
        return (pow(2, n, m) - 2) % m
