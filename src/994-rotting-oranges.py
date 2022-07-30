import collections


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        q = collections.deque()
        result, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx == ROWS or ny == COLS or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    q.append((nx, ny))
                    fresh -= 1
            result += 1

        return result if fresh == 0 else -1
