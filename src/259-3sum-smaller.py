from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()  # nlogn
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target - nums[i]:
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res
