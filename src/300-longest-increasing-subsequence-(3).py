from typing import List
from collections import defaultdict


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # cache = defaultdict(int)
        cache = [1] * len(nums)

        def dfs(i):
            if i == len(nums):
                return 0

            # if i in cache:
            #     return cache[i]

            while (i + 1) < len(nums) and nums[i] >= nums[i + 1]:
                i += 1

            cache[i] += dfs(i + 1)
            return cache[i]

        dfs(0)
        return max(cache)


a = Solution()
nums = [0, 1, 0, 3, 2, 3]
print(a.lengthOfLIS(nums))
