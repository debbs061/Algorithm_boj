class Solution(object):
    def findTargetSumWays(self, nums, target):
        dp = {}

        def dfs(i, sum):
            if i == len(nums):
                return 1 if sum == target else 0
            if (i, sum) in dp:
                return dp[(i, sum)]

            dp[(i, sum)] = dfs(i + 1, sum + nums[i]) + dfs(i + 1, sum - nums[i])
            return dp[(i, sum)]

        return dfs(0, 0)
