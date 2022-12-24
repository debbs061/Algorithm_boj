import heapq
from typing import List
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for u, v, w in times:
            adjList[u].append([v, w])

        q = []
        heapq.heapify(q)
        q.append([0, k])  # curTime, curNode
        result = 1e9
        visit = set()

        while q:
            nodeTime, node = heapq.heappop(q)

            if node in visit:
                continue

            visit.add(node)

            if len(visit) == n:
                result = min(result, nodeTime)
                break

            for adj, w in adjList[node]:
                heapq.heappush(q, [nodeTime + w, adj])

        return -1 if result == 1e9 else result
