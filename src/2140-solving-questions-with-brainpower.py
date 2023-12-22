from typing import List
from collections import defaultdict


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # dp = defaultdict(int)
        # for i in range(len(questions) - 1, -1, -1):
        #     dp[i] = max(questions[i][0] + dp[i + 1 + questions[i][1]], dp[i + 1])
        # return dp[0]

        cache = defaultdict(int)

        def recurse(i):  # i번째에서 끝까지의 max point
            if i >= len(questions):
                return 0
            if i in cache:
                return cache[i]

            # include
            p1 = questions[i][0] + recurse(i + 1 + questions[i][1])
            # not include
            p2 = recurse(i + 1)
            cache[i] = max(p1, p2)
            return cache[i]

        return recurse(0)
