from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(board), len(board[0])

        def dfs(x, y, i):
            if i == len(word):
                return True
            if x < 0 or y < 0 or x == ROWS or y == COLS:
                return False
            if board[x][y] != word[i]:
                return False

            tmp = board[x][y]
            board[x][y] = '#'
            for (dx, dy) in direction:
                nx = x + dx
                ny = y + dy
                if dfs(nx, ny, i + 1):
                    return True

            board[x][y] = tmp
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False
