class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = LinkedList()

    def get(self, index: int) -> int:
        cur = self.head.next
        curIdx = 0
        while cur != None and curIdx < index:
            cur = cur.next
            curIdx += 1

        return -1 if cur is None else cur.val

    # tail 변경 안 됨
    def addAtHead(self, val: int) -> None:
        newNode = LinkedList(val)
        if self.head.next:
            tmp = self.head.next
            self.head.next = newNode
            newNode.next = tmp
        else:
            self.head.next = newNode

    # tail 변경됨
    def addAtTail(self, val: int) -> None:
        newNode = LinkedList(val)
        prev = self.head
        cur = self.head.next

        while cur != None:
            prev = cur
            cur = cur.next

        prev.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:

        newNode = LinkedList(val)
        prev = self.head
        cur = self.head.next
        curIdx = 0
        while cur != None and curIdx < index:
            prev = cur
            cur = cur.next
            curIdx += 1

        if curIdx < index:
            return

        prev.next = newNode
        newNode.next = cur

    def deleteAtIndex(self, index: int) -> None:
        prev = self.head
        cur = self.head.next
        curIdx = 0

        while cur != None and curIdx < index:
            prev = cur
            cur = cur.next
            curIdx += 1

        if curIdx != index:
            return

        prev.next = cur.next if cur else None


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.get(1)
obj.deleteAtIndex(1)
param_1 = obj.get(1)
print(param_1)
