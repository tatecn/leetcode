from math import inf


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = s
        found = False
        n = len(s)
        left = num1 = 0
        for i in range(n):
            if s[i] == '1':
                num1 += 1
            while left < n and s[left] != '1':
                left += 1
            if num1 == k:
                found = True
                cur_str = s[left:i + 1]
                diff = i - left + 1 - len(res)
                if diff < 0 or (diff == 0 and cur_str < res):
                    res = cur_str
                left += 1
                num1 -= 1
        return '' if not found else res

    # def shortestBeautifulSubstring(self, s: str, k: int) -> str:
    #     res = s
    #     found = False
    #     num1 = 0
    #     n = len(s)
    #     num1_idx = [0] * n
    #     cur_left = cur_1_idx = 0
    #     for i in range(n):
    #         if s[i] == '1':
    #             num1 += 1
    #             num1_idx[cur_1_idx] = i
    #             cur_1_idx += 1
    #         if num1 == k:
    #             found = True
    #             cur_str = s[num1_idx[cur_left]:i + 1]
    #             diff = i - num1_idx[cur_left] + 1 - len(res)
    #             if diff < 0 or (diff == 0 and cur_str < res):
    #                 res = cur_str
    #             cur_left += 1
    #             num1 -= 1
    #     return '' if not found else res


s = Solution()
print(s.shortestBeautifulSubstring("100011001", 3) == "11001")
print(s.shortestBeautifulSubstring("1011", 2) == "11")
print(s.shortestBeautifulSubstring("000", 1) == "")
print(s.shortestBeautifulSubstring("001110101101101111", 10) == "10101101101111")
print(s.shortestBeautifulSubstring("1100100101011001001", 7) == "1100100101011")
print(s.shortestBeautifulSubstring("1111111011111", 12) == "1111111011111")
