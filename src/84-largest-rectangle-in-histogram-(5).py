from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # strictly monotonic increasing stack
        res = -1e9
        for curIdx, curHeight in enumerate(heights):
            startIdx = curIdx
            while stack and stack[-1][1] >= curHeight:
                poppedIdx, poppedHeight = stack.pop()
                res = max((curIdx - poppedIdx) * poppedHeight, res)
                startIdx = poppedIdx
            stack.append([startIdx, curHeight])

        # stack 에 남은 elemenet 들은 마지막 인덱스까지 extend 가능
        for curIdx, curHeight in stack:
            res = max(res, (len(heights) - curIdx) * curHeight)

        return res
