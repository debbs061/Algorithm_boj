from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, sum, subset):
            if sum == target:
                result.append(subset.copy())
                return
            if sum > target:
                return
            if i == len(candidates):
                return

            subset.append(candidates[i])
            dfs(i, sum + candidates[i], subset)
            subset.pop()

            dfs(i + 1, sum, subset)

        dfs(0, 0, [])
        return result
