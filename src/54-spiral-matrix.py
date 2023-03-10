from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []

        x, y, d_idx = 0, 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, top

        while len(res) < ROWS * COLS:
            res.append(matrix[x][y])
            matrix[x][y] = None  # mark as visited

            dx, dy = directions[d_idx]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx == ROWS or ny < 0 or ny == COLS or matrix[nx][ny] is None:
                d_idx = (d_idx + 1) % 4
                dx, dy = directions[d_idx]
                nx, ny = x + dx, y + dy

            x, y = nx, ny

        return res
