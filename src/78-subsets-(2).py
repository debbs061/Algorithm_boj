from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []

        def dfs(i):
            if i == len(nums):
                result.append(subset.copy())
                return

            # include
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            # not include
            dfs(i + 1)



        dfs(0)
        return result
