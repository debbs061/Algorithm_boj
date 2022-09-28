from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        buyPrice = 0

        def dfs(i, isBought, total):
            if i >= len(prices):
                return total

            if (i, isBought) in cache:
                return cache[(i, isBought)]

            profit = prices[i] - buyPrice
            totalProfit = total

            if isBought and profit > 0:
                # sell now
                totalProfit = max(totalProfit, dfs(i + 2, False, total + profit))
            elif not isBought:
                # buy now
                totalProfit = max(totalProfit, dfs(i + 1, True, total))

            cache[(i, isBought)] = max(totalProfit, dfs(i + 1, isBought, total))

            return cache[(i, isBought)]

        result = dfs(0, False, 0)
        return result if result > 0 else 0
