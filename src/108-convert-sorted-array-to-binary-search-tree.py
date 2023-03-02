# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursive(l, r):
            if l > r:
                return None
            m = (l + r) // 2

            root = TreeNode(nums[m])
            root.left = recursive(l, m - 1)
            root.right = recursive(m + 1, r)
            return root

        return recursive(0, len(nums) - 1)
