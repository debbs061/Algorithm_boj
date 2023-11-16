from typing import List
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        sortedTrips = sorted(trips, key=lambda x: (x[1], -x[2]))
        curCapacity = 0
        for size, f, t in sortedTrips:
            # 1. heap pop 진행
            while minHeap and minHeap[0][0] <= f:
                topT, topSize, topF = heapq.heappop(minHeap)
                curCapacity -= topSize
            # 2. heap push 진행
            if curCapacity + size > capacity:
                return False
            curCapacity += size
            heapq.heappush(minHeap, [t, size, f])
        return True
