from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)

        result = 0
        for n in nums:
            if (n - 1) not in check:
                length = 0
                while (n + length) in check:
                    length += 1
                result = max(result, length)
        return result
