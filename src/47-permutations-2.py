from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1

        result, perm = [], []

        def dfs():
            if len(nums) == len(perm):
                result.append(perm.copy())
                return

            for n in count:  # only iterate thorugh unique num
                if count[n] > 0:  # there is enough num to pick
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()

        dfs()
        return result
