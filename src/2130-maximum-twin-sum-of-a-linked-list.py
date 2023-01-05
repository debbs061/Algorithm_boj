# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        indexToVal = []
        cur = head
        size = 0
        while cur != None:
            indexToVal.append(cur.val)
            size += 1
            cur = cur.next

        maxTwinSum = 0
        for idx, val in enumerate(indexToVal):
            twinIdx = size - 1 - idx
            if twinIdx >= 0 and twinIdx <= (size / 2) - 1:
                curTwinSum = indexToVal[twinIdx] + val
                maxTwinSum = max(maxTwinSum, curTwinSum)

        return maxTwinSum
