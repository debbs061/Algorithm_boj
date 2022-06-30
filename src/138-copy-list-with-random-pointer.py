"""
# Definition for a Node.

"""


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToCopy = {None: None}

        # 1. just make copied nodes and mapping hashMap
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        # 2. connect next and random pointer
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]  # cur.next 가 null 인 edge case 방어 가능
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]
