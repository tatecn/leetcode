class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c: str) -> int:
            return ord(c) - ord('a') + 1

        n = len(s)
        end = n - k - 1
        hash = 0
        for i in range(n - 1, end, -1):
            hash = (hash * power + val(s[i])) % modulo
            # hash = (
            #                ((hash * (power % modulo)) % modulo)
            #                + (val(s[i]) % modulo)
            #        ) % modulo
        res = end + 1 if hash == hashValue else 0

        pk = pow(power, k, modulo)
        for i in range(end, -1, -1):
            hash = (hash * power + val(s[i]) - pk * val(s[i + k])) % modulo
            # hash = ((hash * power + val(s[i]) % modulo) - ((pk * (val(s[i + k]) % modulo)) % modulo)) % modulo
            if hash == hashValue:
                res = i
        return s[res:res + k]

        # def subStrHash(self, s: str, power: int, mod: int, k: int, hashValue: int) -> str:
    #     n = len(s)
    #     # 用秦九韶算法计算 s[n-k:] 的哈希值
    #     hash = 0
    #     for i in range(n - 1, n - k - 1, -1):
    #         hash = (hash * power + (ord(s[i]) & 31)) % mod
    #     ans = n - k if hash == hashValue else 0
    #     pk = pow(power, k, mod)
    #     # 向左滑窗
    #     for i in range(n - k - 1, -1, -1):
    #         # 计算新的哈希值
    #         hash = (hash * power + (ord(s[i]) & 31) - pk * (ord(s[i + k]) & 31)) % mod
    #         if hash == hashValue:
    #             ans = i
    #     return s[ans: ans + k]

    # Time Limit Exceeded
    # def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    #     def val(c: str) -> int:
    #         return ord(c) - ord('a') + 1
    #
    #     sum_k = 0
    #     for i, c in enumerate(s):
    #         m = i - (k - 1)
    #         if m < 0:
    #             sum_k += val(c) * pow(power, i)
    #             continue
    #         else:
    #             sum_k += val(c) * pow(power, k - 1)
    #         if sum_k % modulo == hashValue:
    #             return s[m:i + 1]
    #         sum_k -= val(s[m])
    #         sum_k = sum_k // power
    #     return ''


s = Solution()
# print(s.subStrHash(s="leetcode", power=7, modulo=20, k=2, hashValue=0) == "ee")
print(s.subStrHash("fbxzaad", 31, 100, 3, 32) == "fbx")
