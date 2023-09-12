# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. 중간 지점(mid) 을 찾는다.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # 2. 중간 지점(mid)부터, 반대 방향으로 돌린다.
        prev, cur = None, mid
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        left, right = head, prev
        # 3. left 와 right 를 시작점으로 Reorder 를 진행한다.
        while left or right:
            if left:
                leftNxt = left.next
                left.next = right
                left = leftNxt
            if right:
                rightNxt = right.next
                right.next = left
                right = rightNxt
