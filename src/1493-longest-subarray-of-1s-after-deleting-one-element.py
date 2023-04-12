from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_allowance = 1
        max_len = 0

        for right in range(len(nums)):
            zero_allowance -= nums[right] == 0

            while zero_allowance < 0:
                zero_allowance += nums[left] == 0
                left += 1

            max_len = max(max_len, right - left)

        return max_len
