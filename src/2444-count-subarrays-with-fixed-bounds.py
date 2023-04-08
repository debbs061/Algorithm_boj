from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        maxIdx = minIdx = lastOutOfBoundsIdx = -1
        result = 0
        for i, n in enumerate(nums):
            if not minK <= n <= maxK:
                lastOutOfBoundsIdx = i
            if n == minK:
                minIdx = i
            if n == maxK:
                maxIdx = i

            result += max(0, min(maxIdx, minIdx) - lastOutOfBoundsIdx)
        return result
