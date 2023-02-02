from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(num, subset):
            if num == n + 1:
                if len(subset) == k:
                    res.append(subset.copy())
                return

            if len(subset) == k:
                res.append(subset.copy())
                return

            # Include num
            subset.append(num)
            dfs(num + 1, subset)
            subset.pop()

            # NOT Include num
            dfs(num + 1, subset)

        dfs(1, [])
        return res
