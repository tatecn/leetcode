class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = n = len(blocks)
        wnum = 0
        for i, c in enumerate(blocks):
            if c == 'W':
                wnum += 1
            if i < k - 1:
                continue
            res = min(res, wnum)
            if blocks[i - (k - 1)] == 'W':
                wnum -= 1
        return res
