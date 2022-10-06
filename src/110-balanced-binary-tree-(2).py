# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # return Height
        balanced = [True]

        def dfs(node):
            if not node:
                return -1

            leftHeight = 1 + dfs(node.left)
            rightHeight = 1 + dfs(node.right)

            if abs(leftHeight - rightHeight) > 1:
                balanced[0] = False
                return max(leftHeight, rightHeight)

            return max(leftHeight, rightHeight)

        dfs(root)
        return balanced[0]
