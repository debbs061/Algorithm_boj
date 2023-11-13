from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePointsInMin = []
        for t in timePoints:
            hh = int(t[:2]) * 60
            mm = int(t[3:])
            timePointsInMin.append(hh + mm)
        timePointsInMin.sort()
        timePointsInMin.append(timePointsInMin[0] + 24 * 60)
        res = 1e9
        for i in range(len(timePointsInMin) - 1):
            res = min(timePointsInMin[i + 1] - timePointsInMin[i], res)
        return res
