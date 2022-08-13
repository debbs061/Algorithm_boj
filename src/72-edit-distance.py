class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[1e9] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # fill the bottom rows
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        # word1 = "horse"
        # word2 = "ros"
        def dfs(i, j):
            if i == len(word1) or j == len(word2):  # 진짜 끝
                return dp[i][j]
            if dp[i][j] != 1e9:
                return dp[i][j]
            if i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                dp[i][j] = dfs(i + 1, j + 1)
            else:
                dp[i][j] = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))

            return dp[i][j]

        return dfs(0, 0)
