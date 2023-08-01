from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []  # monotonic increasing stack

        for i, h in enumerate(heights):
            startIdx = i
            while stack and stack[-1][1] > h:  # 더 이상 확장할 수 없으므로, 넓이 계산해야함
                topIdx, topHeight = stack.pop()
                res = max((i - topIdx) * topHeight, res)
                startIdx = topIdx
            stack.append([startIdx, h])

        lastIdx = len(heights)
        for i, h in stack:
            res = max((lastIdx - i) * h, res)

        return res
