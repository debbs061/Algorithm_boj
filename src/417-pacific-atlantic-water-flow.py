class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(heights), len(heights[0])
        result = []
        pac, atl = set(), set()

        def dfs(x, y, visit, prevHeight):
            if x < 0 or x == ROWS or y == COLS or y < 0 or (x, y) in visit or heights[x][y] < prevHeight:
                return

            visit.add((x, y))
            dfs(x + 1, y, visit, heights[x][y])
            dfs(x - 1, y, visit, heights[x][y])
            dfs(x, y + 1, visit, heights[x][y])
            dfs(x, y - 1, visit, heights[x][y])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])

        return result
