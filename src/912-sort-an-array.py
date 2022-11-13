from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(start, end):
            if start >= end:
                return
            pivot = end
            cur = 0
            for i in range(0, end):
                if nums[i] <= nums[pivot]:
                    nums[i], nums[cur] = nums[cur], nums[i]
                    cur += 1
            nums[cur], nums[pivot] = nums[pivot], nums[cur]
            quickSort(start, cur - 1)
            quickSort(cur + 1, end)

        quickSort(0, len(nums) - 1)
        return nums
