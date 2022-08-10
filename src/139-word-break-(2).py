class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]

            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    if dfs(i + len(word)):
                        dp[i] = True
                        return dp[i]

            dp[i] = False
            return dp[i]

        return dfs(0)

