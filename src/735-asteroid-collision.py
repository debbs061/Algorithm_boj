from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i, a in enumerate(asteroids):
            # 충돌나는 상황
            while stack and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) >= abs(a):
                    if abs(stack[-1]) == abs(a):
                        stack.pop()
                    break
                stack.pop()
            # 충돌나지 않은 상황
            else:
                stack.append(a)
        return stack
