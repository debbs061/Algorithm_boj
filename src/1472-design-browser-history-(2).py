class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.curIdx = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.curIdx += 1
        if len(self.stack) - 1 < self.curIdx:
            # 있으면 덮어쓰거나, 없으면 append
            self.stack.append(url)
        else:
            self.stack[self.curIdx] = url
        self.bound = self.curIdx

    def back(self, steps: int) -> str:
        self.curIdx = max(self.curIdx - steps, 0)
        return self.stack[self.curIdx]

    def forward(self, steps: int) -> str:
        self.curIdx = min(self.curIdx + steps, self.bound)
        return self.stack[self.curIdx]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
