from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ROWS, COLS = len(matrix), len(matrix[0])

        # determine whether the row and col is zero
        isFirstRowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # 동일 선상의 row 를 0 으로
                    if r == 0:
                        isFirstRowZero = True
                    else:
                        matrix[r][0] = 0

                    # 동일 선상의 col 을 0 으로
                    matrix[0][c] = 0

        # make all columns as zeros
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if isFirstRowZero:
            for c in range(COLS):
                matrix[0][c] = 0
