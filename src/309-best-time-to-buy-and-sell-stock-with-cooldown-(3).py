from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices) + 2)

        for i in range(len(prices) - 2, -1, -1):
            for j in range(i + 1, len(prices)):
                # if "i" is included in the transaction
                if prices[j] > prices[i]:
                    dp[i] = max(dp[i], prices[j] - prices[i] + dp[j + 2])
                # if "i" is not included in the transaction
                dp[i] = max(dp[i + 1], dp[i])
        return dp[0]
