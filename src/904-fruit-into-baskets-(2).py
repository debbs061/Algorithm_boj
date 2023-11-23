from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = defaultdict(int)  # lastIdx
        l, r = 0, 0
        for r in range(len(fruits)):
            baskets[fruits[r]] += 1
            if len(baskets) > 2:
                baskets[fruits[l]] -= 1
                if baskets[fruits[l]] == 0:
                    del baskets[fruits[l]]
                l += 1
        return r - l + 1
