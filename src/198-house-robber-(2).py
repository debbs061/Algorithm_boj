from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # return the max money
        result = 0

        one = nums[len(nums) - 1]
        two = 0

        for i in range(len(nums) - 2, -1, -1):
            tmp = one
            one = max(nums[i] + two, one)
            two = tmp

        return one
