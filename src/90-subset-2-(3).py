from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        nums.sort()

        def recurse(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # include
            subset.append(nums[i])
            recurse(i + 1)
            subset.pop()

            # not include
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            recurse(i + 1)

        recurse(0)
        return res
