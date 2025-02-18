class CustomStack:

    def __init__(self, maxSize: int):
        self.data = []
        self.size = maxSize

    def push(self, x: int) -> None:
        self.data.append(x) if len(self.data) < self.size else None

    def pop(self) -> int:
        return self.data.pop() if self.data else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.data))):
            self.data[i] += val
        # n=min(k,len(self.data))
        # for i in range(n):
        #     self.data[i] += val
        # self.data=[self.data[i]+val for i in range(n)]+self.data[n:len(self.data)]
