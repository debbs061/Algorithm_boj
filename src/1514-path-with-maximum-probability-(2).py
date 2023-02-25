import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        max_heap = []
        adj_list = [[] for _ in range(n)]
        visit = set()

        for i, (x, y) in enumerate(edges):
            adj_list[x].append([y, succProb[i]])
            adj_list[y].append([x, succProb[i]])

        heapq.heappush(max_heap, (-1, start))

        while max_heap:
            cost, node = heapq.heappop(max_heap)

            if node in visit:
                continue

            visit.add(node)
            if node == end:
                return -cost

            for adj_node, adj_cost in adj_list[node]:
                if adj_node not in visit:
                    heapq.heappush(max_heap, (cost * adj_cost, adj_node))

        return 0
