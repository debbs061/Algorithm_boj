from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        now, i = 0, 0
        k = 0
        while i < len(nums):
            nums[now] = nums[i]
            k += 1
            while i < len(nums) and nums[now] == nums[i]:  # [1,1,1,2,2,2]
                i += 1
            now = now + 1

        return k
