# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]

        # height of a root = 1 + max(left,right)
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            # diameter
            res[0] = max(res[0], left + right)
            return max(left, right) + 1

        dfs(root)
        return res[0]

