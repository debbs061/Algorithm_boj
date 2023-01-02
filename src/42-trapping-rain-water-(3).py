from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # min(L,R) - h[i]

        maxLeft, maxRight = [], []
        curMax = 0
        for h in height:
            maxLeft.append(curMax)
            if h > curMax:
                curMax = h

        curMax = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight.append(curMax)
            if height[i] > curMax:
                curMax = height[i]

        maxRight = maxRight[::-1]
        answer = 0
        for i in range(len(height)):
            ans = min(maxLeft[i], maxRight[i]) - height[i]
            answer += 0 if ans < 0 else ans

        return answer
