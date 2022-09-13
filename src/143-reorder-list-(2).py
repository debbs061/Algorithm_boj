# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            newNode = oldToCopy[cur]
            newNode.next = oldToCopy[cur.next]
            newNode.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]
