# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find the middle of the list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the half after middle ( 6 -> 5 -> 4 )
        cur = slow.next
        prev = None
        slow.next = None  # Disconnect the connection
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # start reorder one by one
        # 1 -> 2 -> 3
        # 6 -> 5 -> 4
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
