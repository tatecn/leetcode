from collections import defaultdict, Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_s = len(s)
        len_p = len(p)
        if len_s < len_p:
            return res

        cnt = Counter(p)
        left = 0
        for r, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:
                cnt[s[left]] += 1
                left += 1
            if r - left + 1 == len_p:
                res.append(left)

        return res

    # optimize time and space complexity
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     res = []
    #     len_s = len(s)
    #     len_p = len(p)
    #     if len_s < len_p:
    #         return res
    #
    #     a_int = 97
    #     cnt = defaultdict(int)
    #     for c in p:
    #         cnt[ord(c) - a_int] += 1
    #     diff = len(cnt)
    #
    #     left = 0
    #     for r, c in enumerate(s):
    #         cnt[ord(c) - a_int] -= 1
    #         if cnt[ord(c) - a_int] == 0:
    #             diff -= 1
    #         while diff == 0:
    #             if r - left + 1 == len_p:
    #                 res.append(left)
    #             idx = ord(s[left]) - a_int
    #             if cnt[idx] == 0:
    #                 diff += 1
    #             cnt[idx] += 1
    #             left += 1
    #
    #     return res

    # optimized V2
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     res = []
    #     len_s = len(s)
    #     len_p = len(p)
    #     if len_s < len_p:
    #         return res
    #
    #     a_int = 97
    #     cnt_s = [0] * 26
    #     cnt_p = [0] * 26
    #     for i, c in enumerate(p):
    #         cnt_s[ord(s[i]) - a_int] += 1
    #         cnt_p[ord(c) - a_int] += 1
    #     if cnt_s == cnt_p:
    #         res.append(0)
    #
    #     for i in range(len_s - len_p):
    #         cnt_s[ord(s[i]) - a_int] -= 1
    #         cnt_s[ord(s[i + len_p]) - a_int] += 1
    #         if cnt_s == cnt_p:
    #             res.append(i + 1)
    #     return res

    # My version
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     def is_anagram(cnt_1: List[int], cnt_2: List[int]) -> bool:
    #         if len(cnt_1) != len(cnt_2):
    #             return False
    #         for j in range(len(cnt_1)):
    #             if cnt_1[j] != cnt_2[j]:
    #                 return False
    #         return True
    #
    #     res = []
    #     k = len(p)
    #     a_int = 97
    #     cnt_p = [0] * 26
    #     for c in p:
    #         cnt_p[ord(c) - a_int] += 1
    #
    #     cnt_s = [0] * 26
    #     start = 0
    #     for i, c in enumerate(s):
    #         cnt_s[ord(c) - a_int] += 1
    #         if i < k - 1:
    #             continue
    #         start = i - (k - 1)
    #         if is_anagram(cnt_s, cnt_p):
    #             res.append(start)
    #         cnt_s[ord(s[start]) - a_int] -= 1
    #     return res


s = Solution()
print(s.findAnagrams(s="cbaebabacd", p="abc") == [0, 6])
