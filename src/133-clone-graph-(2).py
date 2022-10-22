# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic = {}

        def dfs(node):
            if not node:
                return
            if node.val in dic:
                return dic[node.val]

            newNode = Node(node.val)
            dic[node.val] = newNode

            newNei = []
            for nei in node.neighbors:
                newNei.append(dfs(nei))
            newNode.neighbors = newNei
            return newNode

        return dfs(node)
