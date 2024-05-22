from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        numToFreq = Counter(nums)
        res = 0
        for key in numToFreq:
            anotherKey = key + k
            if anotherKey == key and numToFreq[key] >= 2:
                res += 1
            elif anotherKey != key and anotherKey in numToFreq:
                res += 1
        return res
