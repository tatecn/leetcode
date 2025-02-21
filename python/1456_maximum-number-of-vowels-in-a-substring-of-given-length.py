class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        vowels = set('aeiou')
        n = len(s)
        l = r = 0
        cnt = 0
        while r < n:
            if s[r] in vowels:
                cnt += 1
            if r - l + 1 == k:
                res = max(res, cnt)
                if res == k:
                    break
                if s[l] in vowels:
                    cnt -= 1
                l += 1
            r += 1
        return res


s = Solution()
print(s.maxVowels('abciiidef', 3) == 3)
print(s.maxVowels('aeiou', 2) == 2)
print(s.maxVowels('leetcode', 3) == 2)
