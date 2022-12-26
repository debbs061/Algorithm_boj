import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # build an adjacency list
        adj = {}
        for i in range(len(points)):
            adj[i] = []

        for i in range(len(points)):
            for j in range(1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                w = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([j, w])
                adj[j].append([i, w])

        # Initialize the minHeap
        minHeap = [[0, 0]]

        # find the minimum cost
        result = 0
        visit = set()
        while len(visit) < len(points):
            cost, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            visit.add(n2)
            result += cost
            for x, w in adj[n2]:
                if x not in visit:
                    heapq.heappush(minHeap, [w, x])

        return result
