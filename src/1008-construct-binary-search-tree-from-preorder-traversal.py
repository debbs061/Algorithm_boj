# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def recursive(bound):
            # preorder = [8, 5, 1, 7, 10, 12]
            if not preorder or (bound and preorder[0] > bound):
                return None

            node = TreeNode(preorder.pop(0))
            node.left = recursive(node.val)
            node.right = recursive(bound)
            return node

        return recursive(None)
