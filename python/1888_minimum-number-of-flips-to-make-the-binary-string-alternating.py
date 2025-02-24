from collections import deque


class Solution:

    # V1: easy to understand
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        n2 = 2 * n
        s_1_start, s_0_start = ['0'] * n2, ['0'] * n2
        for i in range(n2):
            if i & 1 == 1:
                s_0_start[i] = '1'
            else:
                s_1_start[i] = '1'

        res_s1 = res_s2 = 0
        res = n
        for i, c in enumerate(s):
            if c != s_1_start[i]:
                res_s1 += 1
            else:
                res_s2 += 1
            if i >= n:
                if s[i - n] != s_1_start[i - n]:
                    res_s1 -= 1
                else:
                    res_s2 -= 1
            if i >= n - 1:
                res = min(res, res_s1, res_s2)
        return res

    # def minFlips(self, s: str) -> int:
    #     n = len(s)
    #     s_1_start, s_0_start = ['0'] * n, ['0'] * n
    #     for i in range(n):
    #         if i & 1 == 1:
    #             s_0_start[i] = '1'
    #         else:
    #             s_1_start[i] = '1'
    #
    #     res_s1 = res_s2 = 0
    #     res = n
    #     d = deque(s)
    #     for i, c in enumerate(s):
    #         if c != s_1_start[i]:
    #             res_s1 += 1
    #         else:
    #             res_s2 += 1
    #     res = min(res, res_s1, res_s2)
    #     for i in range(n - 1):
    #         d.rotate(-1)
    #         if d[-1] != s_1_start[i]:
    #             res_s1 -= 1
    #         else:
    #             res_s2 -= 1
    #         if d[-1] != s_1_start[-(i + 2)]:
    #             res_s1 += 1
    #         else:
    #             res_s2 += 1
    #         res = min(res, res_s1, res_s2)
    #     return res


s = Solution()
print(s.minFlips("111000") == 2)
