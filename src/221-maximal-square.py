from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0
        prev = [0] * (COLS + 1)
        for i in range(1, ROWS + 1):
            tmp = [0] * (COLS + 1)
            for j in range(1, COLS + 1):
                if matrix[i - 1][j - 1] == "1":
                    tmp[j] = min(tmp[j - 1], prev[j], prev[j - 1]) + 1
                    res = max(res, tmp[j])
            prev = tmp
        return res * res
