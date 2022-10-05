# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive(head):
            if not head:
                return
            head.left, head.right = head.right, head.left
            recursive(head.left)
            recursive(head.right)
            return head

        return recursive(root)
