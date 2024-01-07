from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixToFreq = defaultdict(int)
        prefixToFreq[0] = 1
        res, curSum = 0, 0

        for n in nums:
            curSum += n
            remainder = curSum % k
            if remainder in prefixToFreq:
                res += prefixToFreq[remainder]
            prefixToFreq[remainder] += 1

        return res
