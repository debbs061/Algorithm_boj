class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        result = 0
        visit = set()

        def dfs(x, y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x, y) in visit or grid[x][y] == "0":
                return

            visit.add((x, y))

            # 4개 방향 dfs
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visit and grid[i][j] == "1":
                    result += 1
                    dfs(i, j)
        return result
