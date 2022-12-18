from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()  # to track the current path

        crsMap = defaultdict(list)
        for a, b in prerequisites:
            crsMap[a].append(b)

        def dfs(crs):
            if crs in visit:
                return False
            visit.add(crs)

            for pre in crsMap[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)
            crsMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
