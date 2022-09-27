from collections import defaultdict


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        bottomRow = [1] * n

        for i in range(m - 1):
            row = [1] * n
            for j in range(n - 2, -1, -1):
                row[j] = row[j + 1] + bottomRow[j]
            bottomRow = row

        return bottomRow[0]
        # dfs with cache
        # cache = defaultdict(int)
        #
        # directions = [[0, 1], [1, 0]]
        #
        # def dfs(x, y):
        #     if x < 0 or x == m or y < 0 or y == n:
        #         return 0
        #     if x == m - 1 and y == n - 1:
        #         return 1
        #     if (x, y) in cache:
        #         return cache[(x, y)]
        #
        #     for nx, ny in directions:
        #         dx, dy = x + nx, y + ny
        #         cache[(x, y)] += dfs(dx, dy)
        #
        #     return cache[(x, y)]
        #
        # return dfs(0, 0)
