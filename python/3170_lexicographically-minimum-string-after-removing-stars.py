class Solution:

    def clearStars(self, s: str) -> str:
        s = list(s)
        stk = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c == '*':
                for cstk in stk:
                    if cstk:
                        s[cstk.pop()] = '*'
                        break
            else:
                stk[ord(c) - ord('a')].append(i)

        return ''.join(c for c in s if c != '*')

    # V1: Time Limit Exceeded
    # def clearStars(self, s: str) -> str:
    #     del_idx = []
    #     stk = []
    #     for i, c in enumerate(s):
    #         if c == '*':
    #             del_idx.append(stk.pop())
    #             del_idx.append(i)
    #         else:
    #             tmp = []
    #             cnum = ord(c)
    #             while stk and cnum > ord(s[stk[-1]]):
    #                 tmp.append(stk.pop())
    #             stk.append(i)
    #             while tmp:
    #                 stk.append(tmp.pop())
    #     del_set = set(del_idx)
    #     res = []
    #     for i in range(len(s)):
    #         if i not in del_set:
    #             res.append(s[i])
    #     return ''.join(res)
