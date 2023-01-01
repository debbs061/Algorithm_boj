from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, cur, k = 1, 1, 1
        for r in range(1, len(nums)):
            if cur >= 2 and nums[r] == nums[r - 1]:
                continue
            elif cur < 2 and nums[r] == nums[r - 1]:
                nums[l] = nums[r]
                cur += 1
            elif nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                cur = 1
            k += 1
            l += 1
        return k
