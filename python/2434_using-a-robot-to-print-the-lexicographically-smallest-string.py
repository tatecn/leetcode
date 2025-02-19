from collections import Counter
from string import ascii_lowercase


# from collections import deque, OrderedDict

class Solution:
    def robotWithString(self, s: str) -> str:
        res = []
        t_stk = []
        cur_min = 0
        cnt = Counter(s)
        for c in s:
            cnt[c] -= 1
            while cur_min < 25 and cnt[ascii_lowercase[cur_min]] == 0:
                cur_min += 1
            t_stk.append(c)

            while t_stk and t_stk[-1] <= ascii_lowercase[cur_min]:
                res.append(t_stk.pop())
        return "".join(res)

    # V2: suffix_min
    # def robotWithString(self, s: str) -> str:
    #     res = []
    #     t_stk = []
    #     n = len(s)
    #     suffix_min = [''] * n
    #     suffix_min[n - 1] = s[-1]
    #     for i in range(n - 2, -1, -1):
    #         suffix_min[i] = min(s[i], suffix_min[i + 1])
    #
    #     for i, c in enumerate(s):
    #         while t_stk and t_stk[-1] <= suffix_min[i]:
    #             res.append(t_stk.pop())
    #         t_stk.append(c)
    #
    #     while t_stk:
    #         res.append(t_stk.pop())
    #     return "".join(res)

    # V1: my version
    # def robotWithString(self, s: str) -> str:
    #     res = []
    #     t_stk = []
    #     key_idx = dict()
    #     for i, cur_c in enumerate(s):
    #         if cur_c in key_idx:
    #             key_idx[cur_c].append(i)
    #         else:
    #             d = deque()
    #             d.append(i)
    #             key_idx[cur_c] = d
    #     key_idx = OrderedDict(sorted(key_idx.items()))
    #     offset = 0
    #     while key_idx:
    #         items = key_idx.popitem(last=False)
    #         key = items[0]
    #         d = items[1]
    #         while d:
    #             # 打印t中小于等于key的字符
    #             while t_stk and t_stk[-1] <= key:
    #                 res.append(t_stk.pop())
    #
    #             min_idx = d.popleft()
    #             while offset < min_idx:
    #                 cur_c = s[offset]
    #                 # 删除key_idx中cur_c相应的记录
    #                 cur_c_idx_d = key_idx.get(cur_c, None)
    #                 if cur_c_idx_d:
    #                     cur_c_idx_d.popleft()
    #                 if not cur_c_idx_d and cur_c in key_idx:
    #                     del key_idx[cur_c]
    #                 # 将cur_c写到t中
    #                 t_stk.append(cur_c)
    #                 offset += 1
    #             # key itself
    #             t_stk.append(s[min_idx])
    #             offset += 1
    #     # s已经处理完，处理t中可能剩余的字符
    #     while t_stk:
    #         res.append(t_stk.pop())
    #     return ''.join(res)


s = Solution()
print(s.robotWithString("zza") == "azz")
print(s.robotWithString("bac") == "abc")
print(s.robotWithString("bdda") == "addb")
