from typing import List
from dataclasses import dataclass


class Solution:
    @dataclass
    class Node:
        id: int
        type: str
        ts: int

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stk = []
        res = [0] * n
        for log in logs:
            arr = log.split(':')
            cur = self.Node(int(arr[0]), arr[1], int(arr[2]))
            if cur.type == 'end':
                start = stk.pop()
                interval = cur.ts - start.ts + 1
                res[start.id] += interval
                if stk:
                    res[stk[-1].id] -= interval
            else:
                stk.append(cur)
        return res
