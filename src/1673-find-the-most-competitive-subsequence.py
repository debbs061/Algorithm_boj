from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        stack = []
        n = len(nums)
        for idx, val in enumerate(nums):
            while stack and stack[-1] > val and len(stack) + (n - idx) > k:
                stack.pop()
            if len(stack) != k:
                stack.append(val)
        return stack
