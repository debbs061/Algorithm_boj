from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        result = []
        adjList = defaultdict(list)
        for pre, crs in prerequisites:
            adjList[crs].append(pre)
        cache = {}

        def dfs(i, preCrs):
            if i == preCrs:
                return True
            if (i, preCrs) in cache:
                return cache[(i, preCrs)]

            for adj in adjList[i]:
                if dfs(adj, preCrs):
                    cache[(i, preCrs)] = True
                    return cache[(i, preCrs)]

            cache[(i, preCrs)] = False
            return cache[(i, preCrs)]

        for crs1, crs2 in queries:
            if dfs(crs2, crs1):
                result.append(True)
            else:
                result.append(False)

        return result
