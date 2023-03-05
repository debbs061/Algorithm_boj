from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sol 1. Using sum
        # res = len(nums)
        # for i in range(len(nums)):
        #     res += i - nums[i]

        # sol 2. Using bit
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]

        return res
