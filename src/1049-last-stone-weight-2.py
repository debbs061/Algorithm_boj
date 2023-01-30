from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        cache = {}

        def dfs(i, sum_1, sum_2):
            if i == len(stones):
                return abs(sum_1 - sum_2)

            if (i, sum_1, sum_2) in cache:
                return cache[(i, sum_1, sum_2)]

            diff_1 = dfs(i + 1, sum_1 + stones[i], sum_2)
            diff_2 = dfs(i + 1, sum_1, sum_2 + stones[i])
            cache[(i, sum_1, sum_2)] = min(diff_1, diff_2)

            return min(diff_1, diff_2)

        return dfs(0, 0, 0)
