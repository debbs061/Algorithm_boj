import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = {}
        for i in range(1, n + 1):
            adj_list[i] = []

        for u, v, w in times:
            adj_list[u].append((v, w))

        shortest = {}
        min_heap = [[0, k]]  # cost, node
        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node in shortest:
                continue
            shortest[node] = cost

            for tar, w in adj_list[node]:
                if tar not in shortest:
                    heapq.heappush(min_heap, [w + cost, tar])

        return max(shortest.values()) if len(shortest) == n else -1
