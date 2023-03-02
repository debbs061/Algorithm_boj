# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # stack = [(root.left, root.right)]
        # while len(stack) > 0:
        #     left_sub, right_sub = stack.pop()
        #
        #     if not left_sub and not right_sub:
        #         continue
        #     if not left_sub or not right_sub:
        #         return False
        #     if left_sub.val != right_sub.val:
        #         return False
        #
        #     stack.append((left_sub.right, right_sub.left))
        #     stack.append((left_sub.left, right_sub.right))
        # return True

        def recurse(left_sub, right_sub):
            if not left_sub and not right_sub:
                return True
            if not left_sub or not right_sub:
                return False
            if left_sub.val != right_sub.val:
                return False
            return recurse(left_sub.right, right_sub.left) and recurse(left_sub.left, right_sub.right)

        return recurse(root.left, root.right)
