# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        def recurse(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            node = arr[m]
            newNode = TreeNode(node.val)
            newNode.left = recurse(l, m - 1)
            newNode.right = recurse(m + 1, r)
            return newNode

        return recurse(0, len(arr) - 1)
