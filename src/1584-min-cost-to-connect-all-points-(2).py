import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # return the minimum cost to make all points connected
        N = len(points)
        adj = {i: [] for i in range(N)}  # list of [cost, point]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([cost, j])
                adj[j].append([cost, i])

        result = 0
        minHeap = [[0, 0]]  # [cost, point]
        visit = set()
        while len(visit) < N:
            cost, idx = heapq.heappop(minHeap)
            if idx in visit:
                continue
            visit.add(idx)
            result += cost
            for adjCost, adjIdx in adj[idx]:
                if adjIdx not in visit:
                    heapq.heappush(minHeap, [adjCost, adjIdx])

        return result
