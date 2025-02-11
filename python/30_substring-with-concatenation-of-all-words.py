from typing import List
from itertools import permutations
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not s or not words:
            return res
        word_len = len(words[0])
        word_count = len(words)
        substr_len = word_len * word_count
        word_freq = Counter(words)
        index_set = set()
        seen = Counter()
        for offset in range(word_len):
            left = offset
            right = offset
            seen.clear()
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                if word in word_freq:
                    seen[word] += 1

                    while seen[word] > word_freq[word]:
                        seen[s[left:left + word_len]] -= 1
                        left += word_len
                    if right - left == substr_len:
                        index_set.add(left)
                else:
                    seen.clear()
                    left = right
        res.extend(index_set)
        return res

        # Time Limit Exceeded（TLE）
        # res = []
        # if not s or not words:
        #     return res
        # word_len = len(words[0])
        # word_count = len(words)
        # substr_len = word_len * word_count
        # word_freq = Counter(words)
        # seen = Counter()
        # for i in range(len(s) - substr_len + 1):
        #     if i > 0:
        #         seen.clear()
        #     for j in range(word_count):
        #         start = i + j * word_len
        #         word = s[start:start + word_len]
        #         seen[word] += 1
        #         if word not in word_freq or seen[word] > word_freq.get(word):
        #             break
        #     if seen == word_freq:
        #         res.append(i)
        # return res

        # code is easy but performance is not acceptable.
        # wset = set("".join(p) for p in permutations(words))
        # step = len(words[0]) * len(words)
        # res = []
        # for i in range(len(s) - step + 1):
        #     if s[i:i + step] in wset:
        #         res.append(i)
        # return res


s = Solution
# print(s.findSubstring(s, "barfoothefoobarman", ["foo", "bar"]))  # [0,9]
# print(s.findSubstring(s, "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))  # []
# print(s.findSubstring(s, "barfoofoobarthefoobarman", ["bar", "foo", "the"]))  # [6, 9, 12]
# print(s.findSubstring(s, "aaaaaaaaaaaaaa", ["aa", "aa"]))  # [0,1,2,3,4,5,6,7,8,9,10]
# print(s.findSubstring(s, "aaa", ["a", "a"]))  # [0,1]
print(s.findSubstring(s, "dddddddddddd", ["dddd","dddd"]))  # [0,1,2,3,4]