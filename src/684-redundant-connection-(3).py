from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # find a parent of node n
        def find(n):
            while n != par[n]:
                n = par[n]
            return n

        def union(a, b):
            n1, n2 = find(a), find(b)
            if n1 == n2:
                return False

            if rank[n1] > rank[n2]:
                par[n2] = n1
                rank[n1] += rank[n2]
            else:
                par[n1] = n2
                rank[n2] += rank[n1]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
