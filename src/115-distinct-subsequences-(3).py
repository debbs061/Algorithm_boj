class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ROWS, COLS = len(s), len(t)

        bottomRow = [0] * (COLS + 1)
        bottomRow[-1] = 1

        for i in range(ROWS - 1, -1, -1):
            tmpRow = [0] * (COLS + 1)
            tmpRow[-1] = 1
            for j in range(COLS - 1, -1, -1):
                if s[i] == t[j]:
                    tmpRow[j] += bottomRow[j + 1]
                tmpRow[j] += bottomRow[j]
            bottomRow = tmpRow

        return bottomRow[0]
