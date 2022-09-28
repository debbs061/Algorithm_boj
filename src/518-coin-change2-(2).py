from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, remain):
            if remain == 0:
                return 1
            elif remain < 0:
                return 0
            if i == len(coins):
                return 0

            if (i, remain) in cache:
                return cache[(i, remain)]

            cache[(i, remain)] = dfs(i, remain - coins[i])
            cache[(i, remain)] += dfs(i + 1, remain)
            return cache[(i, remain)]

        return dfs(0, amount)
