from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxSize = 0
        stack = []  # pop most recent one

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxSize = max(maxSize, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxSize = max(maxSize, h * (len(heights) - i))

        return maxSize
