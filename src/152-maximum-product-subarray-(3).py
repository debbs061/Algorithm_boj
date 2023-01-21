from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = max(nums)
        curMax, curMin = 1, 1
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            tmp = curMax
            curMax = max(n, curMax * n, curMin * n)
            curMin = min(n, curMin * n, tmp * n)

            largest = max(largest, curMax)
        return largest
