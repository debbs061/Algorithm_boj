import heapq
from typing import List
from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        adjList = defaultdict(list)

        for i, [v1, v2] in enumerate(edges):
            adjList[v1].append([v2, succProb[i]])
            adjList[v2].append([v1, succProb[i]])

        q = [[-1, start]]  # [prob, node] .. maxHeap
        heapq.heapify(q)
        visit = set()

        while q:
            prob, node = heapq.heappop(q)
            prob = -prob

            if node in visit:
                continue

            visit.add(node)

            if node == end:
                return prob

            for adjNode, adjProb in adjList[node]:
                heapq.heappush(q, [-prob * adjProb, adjNode])

        return 0
