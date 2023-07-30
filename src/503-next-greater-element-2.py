from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n
        nums = nums * 2
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                s_idx = stack.pop()
                res[s_idx % n] = nums[i]
            stack.append(i)
        return res

