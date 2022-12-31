from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        sum = 0
        l = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                length = min(length, r - l + 1)
                sum -= nums[l]
                l += 1

        return 0 if length == float('inf') else length
