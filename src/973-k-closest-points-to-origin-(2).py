import heapq
import math


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(points) <= k:
            return points
        minHeap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            minHeap.append([dist, [x, y]])

        heapq.heapify(minHeap)
        result = []
        while k > 0:
            result.append(heapq.heappop(minHeap)[1])
            k -= 1
        return result
