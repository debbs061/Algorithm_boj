# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from leetCode
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)

# my solution
# result = 0
#
# def dfs(self, node, maxNode):
#     if not node:
#         return
#     if node.val >= maxNode:
#         maxNode = node.val
#         self.result += 1
#     self.dfs(node.left, maxNode)
#     self.dfs(node.right, maxNode)
#
# def goodNodes(self, root):
#     """
#     :type root: TreeNode
#     :rtype: int
#     """
#     self.dfs(root, root.val)
#     return self.result
