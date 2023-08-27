class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        b_seens = 0
        for i in range(len(s)):
            if s[i] == "a":
                dp[i] = min(b_seens, dp[i - 1] + 1)
            else:
                b_seens += 1
                dp[i] = dp[i - 1]

        return dp[len(s)-1]
