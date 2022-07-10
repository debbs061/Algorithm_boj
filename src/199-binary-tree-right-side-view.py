from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # from leetCode
    def rightSideView(self, root):
        result = []
        q = deque()
        q.append(root)
        while q:
            qLen = len(q)
            rightSide = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                result.append(rightSide)

        return result
    # My Solution
    # def rightSideView(self, root):
    #     result = []
    #     q = deque()
    #     q.append(root)
    #     while q:
    #         qLen = len(q)
    #         level = []
    #         for i in range(qLen):
    #             node = q.popleft()
    #             if node:
    #                 if not level:
    #                     level.append(node.val)
    #                 q.append(node.right)
    #                 q.append(node.left)
    #         if level:
    #             result.append(level[0])
    #
    #     return result
