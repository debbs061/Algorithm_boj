from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        res = 0  # 초단위
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    fresh += 1
                elif grid[x][y] == 2:
                    q.append([x, y])

        while q and fresh > 0:
            res += 1
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] == 1:
                        fresh -= 1
                        grid[nx][ny] = 2  # 재방문 막기 위해
                        q.append([nx, ny])

        return res if fresh <= 0 else -1

