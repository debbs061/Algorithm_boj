import heapq
from collections import Counter, deque


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # return the least number of units of times
        time = 0
        count = Counter(tasks)  # {"A" : 3, "B" : 2 , "C" : 5}
        maxHeap = [-cnt for cnt in count.values()]  # get the most frequent element first
        heapq.heapify(maxHeap)
        q = deque()

        while maxHeap or q:
            time += 1  # 1s
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])  # 2s

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
