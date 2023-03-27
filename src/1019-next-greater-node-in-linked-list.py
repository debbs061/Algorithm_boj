# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        cur = head
        stack = []  # monotonic decreasing stack

        curIdx = 0
        n = 0
        while cur:
            n += 1
            cur = cur.next
        result = [0] * n

        cur = head
        while cur:
            while stack and stack[-1][0] < cur.val:
                val, idx = stack.pop()
                result[idx] = cur.val
            stack.append((cur.val, curIdx))
            cur = cur.next
            curIdx += 1
        return result
