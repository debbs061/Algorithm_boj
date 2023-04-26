from typing import List
from collections import Counter


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        swaps = 1e9
        one_cnt = nums.count(1)
        nums = nums * 2
        l = 0
        sub_cnt = Counter()
        for r in range(len(nums)):
            sub_cnt[nums[r]] += 1
            if r - l + 1 == one_cnt:
                swaps = min(swaps, one_cnt - sub_cnt[1])
                sub_cnt[nums[l]] -= 1
                l += 1
        return swaps
