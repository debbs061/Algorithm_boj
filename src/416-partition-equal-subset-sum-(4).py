from typing import List


class Solution:
    # dfs with cache solution
    # O(2^n)
    def canPartition(self, nums: List[int]) -> bool:
        targetSum = sum(nums) / 2
        cache = set()

        def recurse(i, sum):
            if sum == targetSum:
                return True
            if sum > targetSum or i == len(nums):
                return False
            if (i, sum) in cache:
                return False

            # include i
            if recurse(i + 1, sum + nums[i]):
                return True

            # not include i
            if recurse(i + 1, sum):
                return True

            cache.add((i, sum))
            return False

        return recurse(0, 0)
