from typing import List
from collections import defaultdict


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)  # dp[i] = i로 시작하는 longest length of LIS

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    # cache = defaultdict(int)
    #
    # def recurse(i):
    #     if i == len(nums):
    #         return 0
    #     if i in cache:
    #         return cache[i]
    #     length = 1
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] < nums[j]:
    #             length = max(length, recurse(j) + 1)
    #     cache[i] = length
    #     return cache[i]
    #
    # res = 1
    # for i in range(len(nums)):
    #     res = max(res, recurse(i))
    # return res
