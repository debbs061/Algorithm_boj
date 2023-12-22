from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        def recurse(l, r, cnt):
            if cnt == 3:
                return nums[r] - nums[l]

            m1 = recurse(l + 1, r, cnt + 1)
            m2 = recurse(l, r - 1, cnt + 1)
            return min(m1, m2)

        nums.sort()
        return recurse(0, len(nums) - 1, 0)
