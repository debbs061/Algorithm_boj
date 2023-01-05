# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head

        leftNode = dummyNode
        rightNode = dummyNode
        while rightNode != None:
            leftNode = leftNode.next
            rightNode = rightNode.next.next if rightNode.next else rightNode.next

        return leftNode
