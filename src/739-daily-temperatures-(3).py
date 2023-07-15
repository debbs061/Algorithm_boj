from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                t_idx = stack.pop()
                answer[t_idx] = idx - t_idx
            stack.append(idx)
        return answer
