from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        curSum, res = 0, 0

        for n in nums:
            curSum += n
            res += prefixSum[curSum - goal]
            prefixSum[curSum] += 1
        return res
