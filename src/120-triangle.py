from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = {}

        def recurse(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            if r == len(triangle) - 1:
                return triangle[r][c]
            minPath = min(recurse(r + 1, c), recurse(r + 1, c + 1))
            cache[(r, c)] = triangle[r][c] + minPath
            return cache[(r, c)]

        return recurse(0, 0)
