import collections


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = res = 0
        maxk = 2
        cnt = collections.defaultdict(int)
        for i in range(len(s)):
            cnt[s[i]] += 1
            while cnt[s[i]] > maxk:
                cnt[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res


s = Solution()
print(s.maximumLengthSubstring("bcbbbcba") == 4)
print(s.maximumLengthSubstring("aaaa") == 2)
