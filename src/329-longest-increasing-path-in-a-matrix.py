from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visit = set()
        cache = {}  # value: longest increasing path
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if (x, y) in visit:
                return False

            if (x, y) in cache:
                return cache[(x, y)]

            longest = 1
            visit.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and ny >= 0 and nx < len(matrix) and ny < len(matrix[0]) and (nx, ny) not in visit and \
                        matrix[nx][ny] > matrix[x][y]:
                    longest = max(dfs(nx, ny) + 1, longest)
                cache[(x, y)] = longest
            visit.remove((x, y))
            return cache[(x,y)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)
        return max(cache.values())


a = Solution()
matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(a.longestIncreasingPath(matrix))
