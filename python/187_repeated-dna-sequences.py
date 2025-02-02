from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        size = 10
        n = len(s)
        if n < size:
            return []
        seen = set()
        duplicates = set()
        for i in range(n - size + 1):
            r = i + size - 1
            cur = s[i:r + 1]
            if cur in seen:
                duplicates.add(cur)
            seen.add(cur)
        return list(duplicates)


s = Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))  # ['AAAAACCCCC', 'CCCCCAAAAA']
