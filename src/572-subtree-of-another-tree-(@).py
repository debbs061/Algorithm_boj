# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result = [False]

        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            if not root:
                return False

            res1 = False
            if subRoot and root.val == subRoot.val:
                res1 = self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)

            res2 = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

            if res1 or res2:
                result[0] = True
                exit(0)

            return False

        dfs(root, subRoot)
        return result[0]
