# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, min, max):
            if not node:
                return True

            if node.val <= min or node.val >= max:
                return False

            return dfs(node.left, min, node.val) and dfs(node.right, node.val, max)

        return dfs(root.left, float("-infinity"), root.val) and dfs(root.right, root.val, float("infinity"))
