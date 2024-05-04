from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        takenHeap = []  # [freeTime, room]
        emptyHeap = [i for i in range(n)]  # [room]
        meetingCnt = [0] * n

        meetings.sort()
        for start, end in meetings:

            # 지금 시점에 free 가 될 수 있는 room 이 있는 지 체크
            while takenHeap and takenHeap[0][0] <= start:
                freeTime, room = heapq.heappop(takenHeap)
                heapq.heappush(emptyHeap, room)

            if not emptyHeap:
                freeTime, room = heapq.heappop(takenHeap)
                start, end = freeTime, freeTime + end - start
                heapq.heappush(emptyHeap, room)

            if emptyHeap:
                room = heapq.heappop(emptyHeap)
                heapq.heappush(takenHeap, [end, room])
                meetingCnt[room] += 1

        return meetingCnt.index(max(meetingCnt))
