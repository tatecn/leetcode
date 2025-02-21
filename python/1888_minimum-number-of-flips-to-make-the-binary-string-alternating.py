class Solution:
    def minFlips(self, s: str) -> int:
        one_diff, zero_diff = 0, 0
        for i, c in enumerate(s):
            if i & 1 == 1:
                if c == '1':
                    one_diff += 1
                else:
                    zero_diff += 1
            else:
                if c == '1':
                    zero_diff += 1
                else:
                    one_diff += 1
        return min(one_diff, zero_diff)
