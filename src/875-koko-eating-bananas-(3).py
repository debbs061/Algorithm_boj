from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def getTotalH(k):
            totalH = 0
            for p in piles:
                totalH += (p // k) + 1 if p % k != 0 else (p // k)
            return totalH

        s, e = 1, max(piles)
        res = 1e9
        while s <= e:
            m = (s + e) // 2
            totalH = getTotalH(m)
            if totalH <= h:
                e = m - 1
                res = min(res, m)
            else:
                s = m + 1
        return int(res)
