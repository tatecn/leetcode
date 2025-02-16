from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        f = [0] * (len(text2) + 1)
        for s in text1:
            pre = 0
            for j, value in enumerate(text2):
                tmp = f[j + 1]
                f[j + 1] = pre + 1 if s == value else max(f[j], f[j + 1])
                pre = tmp
        return f[-1]

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     n1, n2 = len(text1), len(text2)
    #     dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    #     for i in range(n1):
    #         for j in range(n2):
    #             if text1[i] == text2[j]:
    #                 dp[i + 1][j + 1] = dp[i][j] + 1
    #             else:
    #                 dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    #     return dp[n1][n2]


s = Solution()
print(s.longestCommonSubsequence("abcde", "ace") == 3)
# print(s.longestCommonSubsequence("abc", "abc") == 3)
# print(s.longestCommonSubsequence("abc", "def") == 0)
