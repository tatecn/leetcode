class Solution:

    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        left = repeat = 0
        res = 1
        for right in range(1, n):
            repeat += s[right] == s[right - 1]
            if repeat > 1:
                left += 1
                while s[left] != s[left - 1]:
                    left += 1
                repeat -= 1
            res = max(res, right - left + 1)
        return res

    # def longestSemiRepetitiveSubstring(self, s: str) -> int:
    #     n = len(s)
    #     left = right = repeat = 0
    #     res = 0
    #     while right < n:
    #         while repeat <= 1 and right < n:
    #             if right - 1 >= 0 and s[right] == s[right - 1]:
    #                 repeat += 1
    #                 if repeat == 2:
    #                     res = max(res, right - left)
    #                     break
    #             right += 1
    #
    #         while repeat > 1 and left < right:
    #             if left + 1 < n and s[left] == s[left + 1]:
    #                 repeat -= 1
    #             left += 1
    #         res = max(res, right - left + 1 if right < n else right - left)
    #         right += 1
    #     return res


s = Solution()
print(s.longestSemiRepetitiveSubstring("152233") == 5)
print(s.longestSemiRepetitiveSubstring("52233") == 4)
print(s.longestSemiRepetitiveSubstring("5494") == 4)
print(s.longestSemiRepetitiveSubstring("1111111") == 2)
