from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS = len(matrix[0])

        def binarySearchForRow(s, e):
            if s > e:
                return -1  # 답이 없음
            m = (s + e) // 2
            if target >= matrix[m][0] and target <= matrix[m][COLS - 1]:
                return m
            elif target > matrix[m][0]:
                return binarySearchForRow(m + 1, e)
            else:
                return binarySearchForRow(s, m - 1)

        rowIdx = binarySearchForRow(0, len(matrix) - 1)
        if rowIdx == -1:
            return False

        def binarySearch(s, e, rowIdx):
            if s > e:
                return False
            m = (s + e) // 2
            if matrix[rowIdx][m] == target:
                return True
            elif matrix[rowIdx][m] > target:
                return binarySearch(s, m - 1, rowIdx)
            else:
                return binarySearch(m + 1, e, rowIdx)

        return binarySearch(0, len(matrix[0]) - 1, rowIdx)
