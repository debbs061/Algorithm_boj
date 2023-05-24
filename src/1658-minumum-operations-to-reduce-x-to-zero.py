from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # return the minimum number of operations = longest substring its total sum up to 'total-x'

        total = sum(nums)
        curSum = l = 0
        res = -1e9
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum > total - x and l <= r:
                curSum -= nums[l]
                l += 1
            if curSum == total - x:
                res = max(res, r - l + 1)

        if res == -1e9:
            return -1
        else:
            return len(nums) - res
