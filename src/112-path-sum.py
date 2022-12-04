# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recursive(node, subSum):
            if not node:
                return False

            # leaf node 면 subSum 검사
            if not node.left and not node.right:
                if subSum + node.val == targetSum:
                    return True
                return False

            # 아니면, 그대로 traverse
            else:
                if recursive(node.left, subSum + node.val):
                    return True
                if recursive(node.right, subSum + node.val):
                    return True

            return False

        return recursive(root, 0)
