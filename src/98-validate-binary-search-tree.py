# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        def valid(node, lowerBound, upperBound):
            if not node:
                return True
            if not (node.val > lowerBound and node.val < upperBound):
                return False
            return (valid(node.left, lowerBound, node.val) and valid(node.right, node.val, upperBound))

        return valid(root, float("-inf"), float("inf"))
