# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # return node itself
        def dfs(node):
            if not node:
                return None

            leftTail = dfs(node.left)
            rightTail = dfs(node.right)
            if node.left:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            last = rightTail or leftTail or node
            return last

        dfs(root)
