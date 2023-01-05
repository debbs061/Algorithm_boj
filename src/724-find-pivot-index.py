from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = 0
        for n in nums:
            totalSum += n

        leftSum = 0
        for i in range(len(nums)):
            rightSum = totalSum - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1
