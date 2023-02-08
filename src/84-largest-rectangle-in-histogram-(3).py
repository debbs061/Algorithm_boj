from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        # Monotonic Increasing Stack
        for i, h in enumerate(heights):
            startIdx = i
            while stack and stack[-1][1] > h:
                topIdx, topHeight = stack.pop()
                maxArea = max(maxArea, topHeight * (i - topIdx))  # extend backward
                startIdx = topIdx
            stack.append([startIdx, h])

        for (i, h) in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
