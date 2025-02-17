class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        def find_next_valid_char(string: str, index: int) -> int:
            """返回下一个有效字符的索引"""
            skip = 0
            while index >= 0:
                if string[index] == "#":
                    skip += 1
                    index -= 1
                elif skip > 0:
                    skip -= 1
                    index -= 1
                else:
                    break

            return index

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = find_next_valid_char(s, i)
            j = find_next_valid_char(t, j)

            if i < 0 and j < 0:  # 两个都遍历完
                return True
            if i < 0 or j < 0:  # 只有一个遍历完
                return False
            if s[i] != t[j]:  # 比较有效字符
                return False

            i -= 1
            j -= 1

        return True

    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     n1, n2 = len(s), len(t)
    #     i = n1 - 1
    #     j = n2 - 1
    #     i_sharp_num, j_sharp_num = 0, 0
    #     while i >= 0 or j >= 0:
    #         while i >= 0:
    #             if s[i] == "#":
    #                 i_sharp_num += 1
    #                 i -= 1
    #             elif i_sharp_num > 0:
    #                 i -= 1
    #                 i_sharp_num -= 1
    #             else:
    #                 break
    #         while j >= 0:
    #             if t[j] == "#":
    #                 j_sharp_num += 1
    #                 j -= 1
    #             elif j_sharp_num > 0:
    #                 j -= 1
    #                 j_sharp_num -= 1
    #             else:
    #                 break
    #
    #         if i < 0 and j < 0:
    #             return True
    #         elif i < 0 or j < 0:
    #             return False
    #         elif i >= 0 and j >= 0:
    #             if s[i] == t[j]:
    #                 i -= 1
    #                 j -= 1
    #             else:
    #                 return False
    #     return True


# def backspaceCompare(self, s: str, t: str) -> bool:
#     def remove_sharp(input: str) -> str:
#         res = []
#         for c in input:
#             if c != "#":
#                 res.append(c)
#             elif len(res) > 0:
#                 res.pop()
#         return "".join(res)
#
#     return remove_sharp(s) == remove_sharp(t)


s = Solution()
# print(s.backspaceCompare("y#fo##f", "y#f#o##f") == True)
# print(s.backspaceCompare("ab##", "c#d#") == True)
print(s.backspaceCompare("ab#c", "ad#c") == True)
# print(s.backspaceCompare("bxj##tw", "bxj###tw") == True)
