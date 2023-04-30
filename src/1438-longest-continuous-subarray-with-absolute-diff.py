from typing import List
import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        res = 0
        minHeap, maxHeap = [], []

        for idx, num in enumerate(nums):
            heapq.heappush(maxHeap, [-num, idx])
            heapq.heappush(minHeap, [num, idx])
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                l = min(maxHeap[0][1], minHeap[0][1]) + 1
                while maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                while minHeap[0][1] < l:
                    heapq.heappop(minHeap)
            res = max(res, idx - l + 1)
        return res
