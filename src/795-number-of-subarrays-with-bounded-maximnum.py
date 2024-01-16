from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        totalCnt, subCnt = 0, 0
        lastInvalidIdx = -1

        for index, num in enumerate(nums):
            if num < left:
                totalCnt += subCnt
            if num > right:
                subCnt = 0
                lastInvalidIdx = index
            if left <= num <= right:
                subCnt = index - lastInvalidIdx
                totalCnt += subCnt
        return totalCnt
