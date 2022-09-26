from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2

        if sum(nums) % 2 > 0:
            return False

        cache = {}

        def dfs(i, curSum):

            if (i, curSum) in cache:
                return False

            if curSum == target:
                return True

            if curSum > target or i == len(nums):
                return False

            if dfs(i + 1, curSum) or dfs(i + 1, curSum + nums[i]):
                return True

            cache[(i, curSum)] = False
            return False

        return dfs(0, 0)


a = Solution()
nums = [1, 5, 11, 5]
print(a.canPartition(nums))
