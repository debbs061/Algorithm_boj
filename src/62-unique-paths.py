class Solution(object):
    def uniquePaths(self, m, n):
        bottomRow = [1] * n

        for _ in range(m - 1):
            topRow = [1] * n
            for j in range(n - 2, -1, -1):
                topRow[j] = topRow[j + 1] + bottomRow[j]
            bottomRow = topRow

        return bottomRow[0]
