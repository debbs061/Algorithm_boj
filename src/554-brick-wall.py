from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefixToFreq = defaultdict(int)

        for r in wall:
            total = 0
            for c in r[:-1]:
                total += c
                prefixToFreq[total] += 1

        freqList = prefixToFreq.values()
        maxFreq = max(freqList) if freqList else 0
        return len(wall) - maxFreq
