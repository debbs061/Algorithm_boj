import collections


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visit = set()
        maxArea = 0
        m = len(grid)
        n = len(grid[0])

        # bfs
        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visit.add((i, j))
            cnt = 1
            while q:
                x, y = q.popleft()
                direction = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                for nx, ny in direction:
                    if nx in range(m) and ny in range(n) and grid[nx][ny] == 1 and (nx, ny) not in visit:
                        cnt += 1
                        q.append((nx, ny))
                        visit.add((nx, ny))
            return cnt

        # 호출부
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visit:
                    maxArea = max(bfs(i, j), maxArea)

        return maxArea
