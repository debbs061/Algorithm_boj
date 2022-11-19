from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kthIndex = len(nums) - k

        def quickSelect(s, e):
            pivot = nums[e]
            partition = s
            for i in range(s, e):
                if nums[i] < pivot:
                    nums[partition], nums[i] = nums[i], nums[partition]
                    partition += 1
            nums[partition], nums[e] = nums[e], nums[partition]
            if partition == kthIndex:
                return nums[partition]
            elif partition > kthIndex:
                return quickSelect(s, partition - 1)
            else:
                return quickSelect(partition + 1, e)

        return quickSelect(0,len(nums)-1)
