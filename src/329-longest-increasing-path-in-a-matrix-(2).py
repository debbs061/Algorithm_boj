from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ROWS, COLS = len(matrix), len(matrix[0])
        cache = [[1] * COLS for _ in range(ROWS)]

        def dfs(i, j):

            if cache[i][j] != 1:
                return cache[i][j]
            maxNum = 1
            if i + 1 < ROWS and matrix[i][j] < matrix[i + 1][j]:
                maxNum = max(1 + dfs(i + 1, j), maxNum)
            if 0 <= i - 1 and matrix[i][j] < matrix[i - 1][j]:
                maxNum = max(1 + dfs(i - 1, j), maxNum)
            if j + 1 < COLS and matrix[i][j] < matrix[i][j + 1]:
                maxNum = max(1 + dfs(i, j + 1), maxNum)
            if 0 <= j - 1 and matrix[i][j] < matrix[i][j - 1]:
                maxNum = max(1 + dfs(i, j - 1), maxNum)

            cache[i][j] = maxNum

            return cache[i][j]

        res = 1
        for i in range(ROWS):
            for j in range(COLS):
                res = max(dfs(i, j), res)

        return res
