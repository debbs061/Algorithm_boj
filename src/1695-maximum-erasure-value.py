from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # return the maximum sum of unique subarray
        curElements = set()
        l = score = curScore = 0
        for r in range(len(nums)):
            while nums[r] in curElements:
                curElements.remove(nums[l])
                curScore -= nums[l]
                l += 1
            curElements.add(nums[r])
            # calculate sum
            curScore += nums[r]
            score = max(score, curScore)
        return score
