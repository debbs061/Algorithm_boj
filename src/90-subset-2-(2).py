from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        def dfs(i, subset):
            if i == len(nums):
                result.append(subset.copy())
                return

            # include i
            subset.append(nums[i])

            dfs(i + 1, subset)
            subset.pop()

            # not include i
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i = i + 1
            dfs(i + 1, subset)

        dfs(0, [])
        return result
