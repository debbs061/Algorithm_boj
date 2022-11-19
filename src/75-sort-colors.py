from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1

        p = 0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[p] = i
                p += 1
