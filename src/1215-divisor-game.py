#leetCode
dp = [-1] * 1001

def divisorGame(self, n):
    if n == 1:
        return 0
    if dp[n] != -1:
        return dp[n]
    else:
        i = 1
        while i * i <= n:
            if n % i == 0:
                if self.divisorGame(self, n - i) == 0:
                    dp[n] = 1
                    return dp[n]
                if i != 1 and self.divisorGame(self, n - (n / i) == 0):
                    dp[n] = 1
                    return dp[n]
            i += 1
        dp[n] = 0
        return dp[n]


n = int(input())
print(divisorGame(n))
