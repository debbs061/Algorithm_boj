# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = None
        cur = list2
        while cur:
            prev = cur
            cur = cur.next
        lastNode = prev  # last node of list2

        prev = None
        cur = list1
        idx = 0
        while cur:
            if idx == a:
                prev.next = list2
            if idx == b:
                lastNode.next = cur.next
                break
            prev = cur
            cur = cur.next
            idx += 1

        return list1
