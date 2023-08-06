from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []  # [idx, 기준선]
        for i, h in enumerate(height):
            f_idx = len(stack) - 1
            while stack and height[stack[f_idx][0]] < h:
                b_idx, b_base = stack[f_idx][0], stack[f_idx][1]
                if b_base <= h:  # 더 값이 커질 여지가 없으니까, 무조건 pop
                    res += b_base - height[b_idx]
                    stack.pop()
                else: # 더 값이 커질 여지가 있으니까, height 값만 바꿔줌
                    res += h - height[b_idx]
                    height[b_idx] = h
                f_idx -= 1
            base = h if not stack else stack[-1][1]
            stack.append([i, base])

        return res
