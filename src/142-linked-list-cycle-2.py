# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # DO NOT MODIFY THE LINKED-LIST
    # MEMORY - o(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        # when there is no cycle
        if not fast or not fast.next:
            return None

        # find the beginning of a cycle
        slow2 = head
        while True:
            if slow == slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next

        return None
