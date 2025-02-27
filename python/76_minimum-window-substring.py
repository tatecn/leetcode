from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        len_s = len(s)
        len_t = len(t)
        if len_s < len_t:
            return res
        cnt = defaultdict(int)
        for c in t:
            cnt[c] += 1
        diff = len(cnt)
        left = 0
        res_l, res_r = -1, len_s
        for r in range(len_s):
            cnt[s[r]] -= 1
            if cnt[s[r]] == 0:
                diff -= 1
            while diff == 0:
                if r - left < res_r - res_l:
                    res_r, res_l = r, left
                if cnt[s[left]] == 0:
                    diff += 1
                cnt[s[left]] += 1
                left += 1
        return s[res_l:res_r + 1] if res_l >= 0 else res


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC") == "BANC")
# print(s.minWindow("a", "a") == "a")
# print(s.minWindow("a", "aa") == "")
