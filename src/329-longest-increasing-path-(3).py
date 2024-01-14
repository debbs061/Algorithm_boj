from typing import List
from collections import defaultdict


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = defaultdict(int)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y):  # (x,y) 에서 시작할 때의 maxLen 구하기
            if (x, y) in cache:
                return cache[(x, y)]

            maxLen = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx == ROWS or ny == COLS or matrix[nx][ny] <= matrix[x][y]:
                    continue
                maxLen = max(dfs(nx, ny), maxLen)
            cache[(x, y)] = maxLen + 1
            return cache[(x, y)]

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res
