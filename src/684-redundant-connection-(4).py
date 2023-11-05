from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        height = {}
        par = {}
        for i in range(1, len(edges) + 1):
            height[i] = 0
            par[i] = i

        def find(n):  # n의 parent node 를 찾는다.
            parNode = par[n]
            while parNode != par[parNode]:
                parNode = par[par[parNode]]
            return parNode

        def union(n1, n2):  # 두 노드를 잇는다.
            par1, par2 = find(n1), find(n2)
            if par1 == par2:
                return False
            if height[par1] > height[par2]:
                par[par2] = par1
            elif height[par1] < height[par2]:
                par[par1] = par2
            else:
                par[par2] = par1
                height[par1] += 1
            return True

        res1, res2 = -1, -1
        for n1, n2 in edges:
            if not union(n1, n2):
                res1, res2 = n1, n2
        return res1, res2
