class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        curMax, curMin = 1, 1
        for n in nums:
            curMax, curMin = max(n, curMax * n, curMin * n), min(n, curMin * n, curMax * n)
            res = max(curMax, res)

        return res
