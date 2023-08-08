from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []
        curMax = 0

        for h in height:
            left.append(curMax)
            curMax = max(curMax, h)

        curMax = 0
        for i in range(len(height) - 1, -1, -1):
            right.append(curMax)
            curMax = max(curMax, height[i])

        right = right[::-1]
        res = 0
        for i in range(len(height)):
            res += max(min(left[i], right[i]) - height[i], 0)

        return res
