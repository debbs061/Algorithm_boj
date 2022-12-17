from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if (i, j) in visit or i < 0 or i == ROWS or j < 0 or j == COLS or grid[i][j] == "0":
                return

            visit.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visit and grid[i][j] == "1":
                    dfs(i, j)
                    result += 1
        return result
