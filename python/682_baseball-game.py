from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        sum = 0
        for s in operations:
            if s == "+":
                val = nums[-1] + nums[-2]
                nums.append(val)
                sum += val
            elif s == "D":
                val = 2 * nums[-1]
                nums.append(val)
                sum += val
            elif s == "C":
                val = nums.pop()
                sum -= val
            else:
                val = int(s)
                nums.append(val)
                sum += val
        return sum
