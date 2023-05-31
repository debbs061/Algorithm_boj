# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next

        l, r = 0, len(arr) - 1
        res = -1e9
        while l < r:
            res = max(res, arr[l] + arr[r])
            l += 1
            r -= 1

        return res
