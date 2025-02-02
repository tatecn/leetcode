class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        existed = set()
        for i in range(len(s)):
            while s[i] in existed:
                existed.remove(s[l])
                l += 1
            res = max(i - l + 1, res)
            existed.add(s[i])
        return res
