from typing import List
from collections import defaultdict


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if stones[0] != 0 or stones[1] != 1:
            return False

        posToIdx = {}
        for i, pos in enumerate(stones):
            posToIdx[pos] = i
        cache = defaultdict(bool)

        def recurse(i, k):
            if i == len(stones) - 1:
                return True
            if (i, k) in cache:
                return cache[(i, k)]

            canComplete = False
            if stones[i] + k in posToIdx:
                canComplete = recurse(posToIdx[stones[i] + k], k)
            if not canComplete and k - 1 != 0 and stones[i] + k - 1 in posToIdx:
                canComplete = recurse(posToIdx[stones[i] + k - 1], k - 1)
            if not canComplete and stones[i] + k + 1 in posToIdx:
                canComplete = recurse(posToIdx[stones[i] + k + 1], k + 1)

            cache[(i, k)] = canComplete
            return cache[(i, k)]

        return recurse(1, 1)
