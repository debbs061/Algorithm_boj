from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        j, sum = 0, 0

        while j < len(nums):
            if sum < 0:
                sum = 0
            sum += nums[j]
            result = max(result, sum)
            j += 1

        return result
