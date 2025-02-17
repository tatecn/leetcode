from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        p = "Push"
        o = "Pop"
        j = 1
        for i in range(len(target)):
            while j < target[i]:
                res.append(p)
                res.append(o)
                j += 1
            res.append(p)
            j += 1
        return res
