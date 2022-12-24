import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = [[grid[0][0], (0, 0)]]  # t, point
        heapq.heapify(q)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()

        while q:
            val = heapq.heappop(q)
            t = val[0]
            x, y = val[1][0], val[1][1]

            if x == ROWS - 1 and y == COLS - 1:
                return t
            if (x, y) in visit:
                continue
            visit.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if min(nx, ny) < 0 or nx == ROWS or ny == COLS:
                    continue
                if grid[nx][ny] <= t:
                    heapq.heappush(q, [t, (nx, ny)])
                else:
                    newT = grid[nx][ny]
                    heapq.heappush(q, [newT, (nx, ny)])
