from typing import List


# O(nLogn) ?
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sub = []
        candidates.sort()

        def dfs(i, sum):
            if sum == target:
                result.append(sub.copy())
                return
            if sum > target:
                return
            if i == len(candidates):
                return

            sub.append(candidates[i])
            dfs(i + 1, sum + candidates[i])
            sub.pop()

            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sum)

        dfs(0, 0)
        return result
