# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1, prev2 = None, None
        while l1 or l2:
            if l1:
                nxt1 = l1.next
                l1.next = prev1
                prev1 = l1
                l1 = nxt1
            if l2:
                nxt2 = l2.next
                l2.next = prev2
                prev2 = l2
                l2 = nxt2

        head1, head2 = prev1, prev2
        bonus = 0
        newNxt = None
        while head1 and head2:
            newVal = head1.val + head2.val + bonus
            newNode = ListNode(newVal % 10)
            bonus = newVal // 10
            newNode.next = newNxt
            newNxt = newNode

            head1 = head1.next
            head2 = head2.next

        while head1:
            newVal = head1.val + bonus
            newNode = ListNode(newVal % 10)
            bonus = newVal // 10
            newNode.next = newNxt
            newNxt = newNode
            head1 = head1.next

        while head2:
            newVal = head2.val + bonus
            newNode = ListNode(newVal % 10)
            bonus = newVal // 10
            newNode.next = newNxt
            newNxt = newNode
            head2 = head2.next

        if bonus > 0:
            print(bonus)
            newNode = ListNode(bonus)
            newNode.next = newNxt
            newNxt = newNode

        return newNxt
