import heapq


class MedianFinder(object):

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num):
        heapq.heappush(self.smallHeap, -num)

        if self.smallHeap and self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            heapq.heappush(self.largeHeap, -heapq.heappop(self.smallHeap))

        if abs(len(self.smallHeap) - len(self.largeHeap)) >= 2:
            if len(self.smallHeap) > len(self.largeHeap):
                heapq.heappush(self.largeHeap, -heapq.heappop(self.smallHeap))
            else:
                heapq.heappush(self.smallHeap, -heapq.heappop(self.largeHeap))

    def findMedian(self):
        lenSmall = len(self.smallHeap)
        lenLarge = len(self.largeHeap)

        if lenSmall > lenLarge:
            return -self.smallHeap[0]
        elif lenLarge > lenSmall:
            return self.largeHeap[0]
        return (-self.smallHeap[0] + self.largeHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
