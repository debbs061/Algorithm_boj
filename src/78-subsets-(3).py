from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subSet = []

        def dfs(i, subSet):
            if i == len(nums):
                res.append(subSet.copy())
                return

            # 현재 수를 포함한다
            subSet.append(nums[i])
            dfs(i + 1, subSet)
            subSet.pop()
            dfs(i + 1, subSet)

        dfs(0, subSet)
        return res
