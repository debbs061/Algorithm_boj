from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        lastEnd = intervals[0][1]
        removal = 0
        for x, y in intervals[1:]:
            if lastEnd > x:
                lastEnd = min(lastEnd, y)
                removal += 1
            else:
                lastEnd = y
        return removal
