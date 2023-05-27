from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def recurse(l, r):
            if l > r:
                return None
            val, idx = -1e9, -1e9
            for i in range(l, r + 1):
                if val < nums[i]:
                    val = nums[i]
                    idx = i
            node = TreeNode(nums[idx])
            node.left = recurse(l, idx - 1)
            node.right = recurse(idx + 1, r)
            return node

        return recurse(0, len(nums) - 1)


