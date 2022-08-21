import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # adjacency list
        adj = {i: [] for i in range(N)}  # [cost, point]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # make edges
        result = 0
        visit = set()
        minHeap = [[0, 0]]  # [cost, node]

        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            result += cost
            for adjCost, adjIndex in adj[i]:
                if adjIndex in visit:
                    continue
                heapq.heappush(minHeap, [adjCost, adjIndex])

        return result
