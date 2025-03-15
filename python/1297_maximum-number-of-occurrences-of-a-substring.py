import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        def val(s: str) -> int:
            return ord(s[0]) - ord('a')

        m = 1_000_000_000 + 7
        base = 26
        n = len(s)
        res = 0
        l_dict = collections.defaultdict(int)
        occ_dict = collections.defaultdict(int)
        k = minSize
        base_k = pow(base, k, m)
        hash = 0
        for i in range(k):
            l_dict[s[i]] += 1
            hash = (hash * base + val(s[i])) % m

        if len(l_dict) <= maxLetters:
            old_hash = occ_dict[hash]
            occ_dict[hash] = old_hash + 1
            if old_hash + 1 > res:
                res = old_hash + 1

        for i in range(k, n):
            l_dict[s[i]] += 1
            pre = i - k
            hash = (hash * base + val(s[i]) - base_k * val(s[pre])) % m
            if l_dict[s[pre]] == 1:
                del l_dict[s[pre]]
            else:
                l_dict[s[pre]] -= 1
            if len(l_dict) <= maxLetters:
                old_hash = occ_dict[hash]
                occ_dict[hash] = old_hash + 1
                if old_hash + 1 > res:
                    res = old_hash + 1

        return res


s = Solution()
print(s.maxFreq("aababcaab", 2, 3, 4) == 2)
print(s.maxFreq("aaaa", 1, 3, 3) == 2)
