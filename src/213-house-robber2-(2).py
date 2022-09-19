from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # 뒤에 하나 빠진거 nums = [2,3,2]
        one, two = nums[len(nums) - 2], 0
        for i in range(len(nums) - 3, -1, -1):
            tmp = one
            one = max(nums[i] + two, one)
            two = tmp

        # 앞에 하나 빠진거
        one2, two2 = nums[len(nums) - 1], 0
        for i in range(len(nums) - 2, 0, -1):
            tmp = one2
            one2 = max(nums[i] + two2, one2)
            two2 = tmp

        return max(one, one2)
