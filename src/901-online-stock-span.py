class StockSpanner:

    def __init__(self):
        self.arr = []  # original
        self.stack = []  # index 를 담는다.

    def next(self, price: int) -> int:
        self.arr.append(price)
        curIdx = len(self.arr) - 1
        lastIdx = curIdx

        if self.arr and self.arr[-1] <= price:
            while self.stack and self.arr[self.stack[-1]] <= price:
                lastIdx = self.stack.pop()

        self.stack.append(lastIdx)
        return curIdx - lastIdx + 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
