class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS, COLS = len(word1), len(word2)
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            dp[r][COLS] = ROWS - r
        for c in range(COLS):
            dp[ROWS][c] = COLS - c
        dp[ROWS][COLS] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if word1[r] == word2[c]:
                    # equal
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    # replace, delete, insert
                    dp[r][c] = min(dp[r + 1][c + 1] + 1, dp[r][c + 1] + 1, dp[r + 1][c] + 1)

        return dp[0][0]
