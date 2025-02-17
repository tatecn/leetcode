class BrowserHistory:

    def __init__(self, homepage: str):
        self.fwd = []
        self.history = []
        self.cur = homepage

    def visit(self, url: str) -> None:
        self.history.append(self.cur)
        self.cur = url
        self.fwd.clear()

    def back(self, steps: int) -> str:
        res = self.cur
        while self.history and steps:
            self.fwd.append(self.cur)
            res = self.history.pop()
            self.cur = res
            steps -= 1
        return res

    def forward(self, steps: int) -> str:
        res = self.cur
        while self.fwd and steps:
            self.history.append(self.cur)
            res = self.fwd.pop()
            self.cur = res
            steps -= 1
        return res


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

obj = BrowserHistory("leetcode.com")
print(None)
print(obj.visit("google.com"))
print(obj.visit("facebook.com"))
print(obj.visit("youtube.com"))
print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))
print(obj.visit("linked.com"))
print(obj.forward(2))
print(obj.back(2))
print(obj.back(7))
