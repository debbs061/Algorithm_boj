from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        sRow, eRow = 0, ROWS - 1
        while sRow <= eRow:
            midRow = (sRow + eRow) // 2
            if target < matrix[midRow][0]:
                eRow = midRow - 1
            elif target > matrix[midRow][-1]:
                sRow = midRow + 1
            else:
                break

        if not (sRow <= eRow):
            return False
        row = (sRow + eRow) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True

        return False
