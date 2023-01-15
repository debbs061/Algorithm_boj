import heapq


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def makeLengthSame(self):
        maxLen, minLen = len(self.maxHeap), len(self.minHeap)
        if abs(minLen - maxLen) >= 2:
            if minLen < maxLen:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            else:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, num)
        if len(self.minHeap) > 0:
            maxVal, minVal = self.maxHeap[0], -self.minHeap[0]
            if maxVal < minVal:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        self.makeLengthSame()

    def findMedian(self) -> float:
        maxLen, minLen = len(self.maxHeap), len(self.minHeap)
        if maxLen > minLen:
            return self.maxHeap[0]
        elif maxLen < minLen:
            return -self.minHeap[0]
        else:
            return (-self.minHeap[0] + self.maxHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
