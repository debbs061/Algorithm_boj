# leetcode 1137. n-th tribonacci number

class Solution(object):
    dp = [0] * 38  # 0~37
    dp[1] = 1
    dp[2] = 1

    def tribonacci(self, n):
        for i in range(3, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2] + self.dp[i - 3]
        return self.dp[n]
