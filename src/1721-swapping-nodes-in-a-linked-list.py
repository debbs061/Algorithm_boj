# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        lastIdx = length - k + 1  # (1-indexed)

        swap1, swap2 = None, None
        idx = 1
        cur = head
        while cur:
            if idx == k:
                swap1 = cur
            if idx == lastIdx:
                swap2 = cur
            if swap1 and swap2:
                break
            cur = cur.next
            idx += 1

        swap1.val, swap2.val = swap2.val, swap1.val
        return head
