import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] = -stones[i]

        while len(stones) > 1:
            heapq.heapify(stones)
            y, x = -heapq.heappop(stones), -heapq.heappop(stones)  # y >= x
            if y > x:
                heapq.heappush(stones, -(y - x))
        return 0 if len(stones) == 0 else -stones[0]
