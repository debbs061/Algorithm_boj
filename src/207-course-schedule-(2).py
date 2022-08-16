import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visit = set()
        cache = {}

        # adjacent list
        adjacentList = collections.defaultdict(list)  # { "a" : [b,c, ...] }
        for a, b in prerequisites:
            adjacentList[a].append(b)  # a를 수강하려면 b를 먼저 수강해야한다.

        def dfs(i):
            if i in visit:
                return False
            if i in cache:
                return cache[i]

            visit.add(i)
            for edges in adjacentList[i]:
                if not dfs(edges):
                    return False
            visit.remove(i)

            cache[i] = True
            return cache[i]

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
