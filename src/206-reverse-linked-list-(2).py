# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, cur):
            if cur is None:
                return prev

            newNext = cur.next
            cur.next = prev
            return reverse(cur, newNext)

        return reverse(None, head)
