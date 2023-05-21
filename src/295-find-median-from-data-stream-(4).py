import heapq


class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:  # o(logn)
        heapq.heappush(self.smallHeap, -num)
        if self.smallHeap and self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            val = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
        if len(self.smallHeap) < len(self.largeHeap):
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -val)
        elif len(self.smallHeap) > len(self.largeHeap) + 1:
            val = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

    def findMedian(self) -> float:  # o(1)
        total = len(self.smallHeap) + len(self.largeHeap)
        if total % 2:  # odd
            return -self.smallHeap[0]
        else:
            return (-self.smallHeap[0] + self.largeHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
