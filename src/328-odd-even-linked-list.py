# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            odd, even = head, head.next
        else:
            return head

        dummy = ListNode()
        dummy.next = head

        start = even

        while odd and even:
            if even.next:
                odd.next = even.next
                odd = even.next
            else:
                break

            even.next = odd.next if odd else None
            even = odd.next if odd else None

        odd.next = start

        return dummy.next
