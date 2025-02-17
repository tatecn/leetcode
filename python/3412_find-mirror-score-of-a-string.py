import string


class Solution:

    def calculateScore(self, s: str) -> int:
        stacks = [[] for _ in range(26)]
        sum = 0
        for i, c in enumerate(map(ord, s)):
            c -= ord('a')
            if stacks[25 - c]:
                cm_i = stacks[25 - c].pop()
                sum += i - cm_i
            else:
                stacks[c].append(i)
        return sum

    # def calculateScore(self, s: str) -> int:
    #     mirror = {k: v for k, v in zip(string.ascii_lowercase, reversed(string.ascii_lowercase))}
    #     char_ods = {k: [] for k in string.ascii_lowercase}
    #     sum = 0
    #     for i, c in enumerate(s):
    #         cm = mirror[c]
    #         cm_od = char_ods[cm]
    #         if cm_od:
    #             cm_i = cm_od.pop()
    #             sum += i - cm_i
    #         else:
    #             char_ods[c].append(i)
    #     return sum


s = Solution()
print(s.calculateScore("aczzx") == 5)
