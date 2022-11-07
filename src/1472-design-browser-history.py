class DoubleLinkedList:
    def __init__(self, url='', prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        newNode = DoubleLinkedList(homepage)
        self.cur = newNode  # 현재 위치한 url

    def visit(self, url: str) -> None:
        newNode = DoubleLinkedList(url)
        self.cur.next = newNode
        newNode.prev = self.cur
        self.cur = newNode

    def back(self, steps: int) -> str:
        next = self.cur.next
        curr = self.cur
        while curr and steps > 0:
            next = curr
            curr = curr.prev
            steps -= 1

        curr = curr if curr else next
        self.cur = curr
        return curr.url

    def forward(self, steps: int) -> str:
        prev = self.cur.prev
        curr = self.cur
        while curr and steps > 0:
            prev = curr
            curr = curr.next
            steps -= 1

        curr = curr if curr else prev
        self.cur = curr
        return curr.url

    # Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
