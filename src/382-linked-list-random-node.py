# Definition for singly-linked list.
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        cur, idx, res = self.head, 0, self.head

        while cur:
            if random.randint(0, idx) == 0:
                res = cur
            idx += 1
            cur = cur.next
        return res.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
