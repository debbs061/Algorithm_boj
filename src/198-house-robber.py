class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        d = [0] * len(nums)
        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            d[i] = max(d[i-2] + nums[i] , d[i-1])
        return d[len(nums) -1]
