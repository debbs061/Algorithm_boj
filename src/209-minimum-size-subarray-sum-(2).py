from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = curSum = 0
        res = 1e9
        for r in range(len(nums)):
            curSum += nums[r]
            while l <= r and curSum >= target:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1

        return res if res != 1e9 else 0
