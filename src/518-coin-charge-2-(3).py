from typing import List


class Solution:
    # time : o(amount*len(coins))
    # memory : o(amount*len(coins))
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for t in range(amount + 1):
                if t - c >= 0:
                    dp[t] += dp[t - c]

        return dp[amount]  # number of combinations
