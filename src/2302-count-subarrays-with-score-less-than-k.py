from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = res = score = curSum = 0

        for r in range(len(nums)):
            curSum += nums[r]
            score = curSum * (r - l + 1)
            while l < len(nums) and score >= k:
                curSum -= nums[l]
                l += 1
                score = curSum * (r - l + 1)
            res += r - l + 1

        return res
