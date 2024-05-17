from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = defaultdict(int)
        curSum = 0
        prefixSum[0] = 1
        for n in nums:
            curSum += n
            excludeSum = curSum - k
            if excludeSum in prefixSum:
                res += prefixSum[excludeSum]
            prefixSum[curSum] += 1

        return res
