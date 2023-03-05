# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        former = head
        latter = prev
        while latter:
            if former.val != latter.val:
                return False
            former = former.next
            latter = latter.next

        return True
