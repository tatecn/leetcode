class MinStack:

    def __init__(self):
        self.data = []
        self.min_stk = []
        self.min = None

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.min_stk and val >= self.min:
            self.min_stk[-1].append(val)
        else:
            self.min = val
            self.min_stk.append([val])

    def pop(self) -> None:
        if self.data:
            self.data.pop()
        if self.min_stk:
            self.min_stk[-1].pop()
        if not self.min_stk[-1]:
            self.min_stk.pop()
            self.min = self.min_stk[-1][0] if self.min_stk else None

    def top(self) -> int:
        return self.data[-1] if self.data else -1

    def getMin(self) -> int:
        return self.min

    # V1: easy to understand
    # def __init__(self):
    #     self.data = []
    #     self.min_stk = []
    #
    # def push(self, val: int) -> None:
    #     self.data.append(val)
    #     if self.min_stk:
    #         self.min_stk.append(min(self.min_stk[-1], val))
    #     else:
    #         self.min_stk.append(val)
    #
    # def pop(self) -> None:
    #     if self.data:
    #         self.data.pop()
    #     if self.min_stk:
    #         self.min_stk.pop()
    #
    # def top(self) -> int:
    #     return self.data[-1] if self.data else -1
    #
    # def getMin(self) -> int:
    #     return self.min_stk[-1] if self.min_stk else -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
print(None)
# print(minStack.push(-2))
# print(minStack.push(0))
# print(minStack.push(-3))
# print(minStack.getMin())  # return -3
# print(minStack.pop())
# print(minStack.top())  # return 0
# print(minStack.getMin())  # return -2

# print(minStack.push(-2))
# print(minStack.push(0))
# print(minStack.push(-1))
# print(minStack.getMin())  # return -2

print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.getMin())  # return -3
print(minStack.pop())
print(minStack.top())  # return 0
print(minStack.getMin())  # return -2
