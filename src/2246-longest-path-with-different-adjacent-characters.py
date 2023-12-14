from typing import List
from collections import defaultdict
import heapq


class Solution:
    def __init__(self):
        self.res = 0

    def longestPath(self, parent: List[int], s: str) -> int:
        cache = defaultdict(int)  # { node : length }
        parToChild = defaultdict(list)  # {0:[2,1]}
        for child, par in enumerate(parent):
            parToChild[par].append(child)

        # 노드 i 부터 leaf 노드까지의 최댓값
        def recurse(i):
            if i in cache:
                return cache[i]

            minHeap = []

            # check if children is same char
            for child in parToChild[i]:
                if s[child] != s[i]:
                    childMaxLength = recurse(child)
                    heapq.heappush(minHeap, -childMaxLength)

            cache[i] = 1
            # if 노드 i 가 root 인 경우, 최대 2개값 계산
            if len(minHeap) >= 2:
                firstMax, secondMax = -heapq.heappop(minHeap), -heapq.heappop(minHeap)
                self.res = max(self.res, firstMax + secondMax + 1)
                cache[i] += firstMax
            elif len(minHeap) == 1:
                firstMax = -heapq.heappop(minHeap)
                cache[i] += firstMax
            return cache[i]

        # traverse child
        for i in range(len(parent)):
            maxLenForPathFromI = recurse(i)
            self.res = max(self.res, maxLenForPathFromI)
        return self.res
