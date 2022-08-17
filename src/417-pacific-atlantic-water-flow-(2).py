class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific, atlantic = set(), set()

        direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(x, y, sea):
            if x < 0 or y < 0 or x == ROWS or y == COLS:
                return
            if (x, y) in sea:
                return

            sea.add((x, y))
            for dx, dy in direction:
                nx, ny = dx + x, dy + y
                if nx < 0 or ny < 0 or nx == ROWS or ny == COLS or heights[x][y] > heights[nx][ny]:
                    continue
                dfs(x + dx, y + dy, sea)

        # pacific ocean - left,top
        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        result = []
        # check if coords in both
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result


