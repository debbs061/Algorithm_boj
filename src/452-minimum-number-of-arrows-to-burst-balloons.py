from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 0
        points.sort()
        currentEnd = points[0][1]
        for x1, x2 in points[1:]:
            if currentEnd < x1:  # 안 겹치는 경우, 이전 풍선 burst!
                res += 1
                currentEnd = x2
            else:  # 겹치는 경우, keep going!
                currentEnd = min(currentEnd, x2)
        return res + 1
