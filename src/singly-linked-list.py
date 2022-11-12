class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def insertEnd(self, val):
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        cur = self.head

        # find the node ahead of the index node (cur)
        while cur and i < index:
            cur = cur.next
            i += 1

        # remove the index node
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
