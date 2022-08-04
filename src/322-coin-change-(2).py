class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        d = [1e9] * (amount + 1)
        d[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    d[i] = min(d[i], 1 + d[i - coin])

        return d[amount] if d[amount] != 1e9 else -1
