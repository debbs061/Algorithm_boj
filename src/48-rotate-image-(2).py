from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        l, r = 0, n - 1

        while l < r:
            top, bottom = l, r

            for i in range(r - l):
                topLeft = matrix[top][l + i]

                # move bottomLeft to topLeft
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottomRight to bottomLeft
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move topRight to bottomRight
                matrix[bottom][r - i] = matrix[top + i][r]

                # move topLeft to topRight
                matrix[top + i][r] = topLeft

            l, r = l + 1, r - 1
