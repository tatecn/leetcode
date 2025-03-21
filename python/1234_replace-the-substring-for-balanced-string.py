from collections import Counter
import math


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        m = n // 4
        cnt = Counter(s)
        if len(cnt) == 4 and min(cnt.values()) == m:
            return 0
        res, left = math.inf, 0
        for i, c in enumerate(s):
            cnt[c] -= 1
            while max(cnt.values()) <= m:
                res = min(res, i - left + 1)
                cnt[s[left]] += 1
                left += 1
        return res


s = Solution()
print(s.balancedString("QQQW") == 2)
