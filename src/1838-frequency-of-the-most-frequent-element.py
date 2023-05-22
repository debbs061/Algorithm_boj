from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # return the maximum frequency
        nums.sort()
        res = total = l = r = 0
        while r < len(nums):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            res = max(r - l + 1, res)
            r += 1
        return res
