from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        courses = defaultdict(list)
        cycle = set()
        visit = set()

        for x, y in prerequisites:
            courses[x].append(y)

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            visit.add(course)
            for pre in courses[course]:
                if not dfs(pre):
                    return False
            result.append(course)
            cycle.remove(course)
            courses[course] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return result
