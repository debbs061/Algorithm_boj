# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from queue import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur, prev):
            if not cur:
                return prev
            else:
                nextNode = cur.next
                cur.next = prev
                return reverse(nextNode, cur)

        return reverse(head, None)
