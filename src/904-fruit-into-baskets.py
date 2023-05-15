from typing import List
from collections import Counter


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res, l = 0, 0
        type = Counter()
        for r in range(len(fruits)):
            while len(type) == 2 and fruits[r] not in type:
                type[fruits[l]] -= 1
                if type[fruits[l]] == 0:
                    del type[fruits[l]]
                l += 1
            type[fruits[r]] += 1
            res = max(r - l + 1, res)
        return res
