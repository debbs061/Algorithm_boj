from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        l = res = 0
        curProd = 1
        for r in range(len(nums)):
            curProd *= nums[r]
            while l <= r and curProd >= k:
                curProd = curProd // nums[l]
                l += 1
            res += r - l + 1

        return res
