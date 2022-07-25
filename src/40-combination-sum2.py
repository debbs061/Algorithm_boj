class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        candidates = sorted(candidates)

        def dfs(i, target, subset):
            if target == 0:
                result.append(subset[::])
                return
            if i >= len(candidates):
                return
            if target < 0:
                return



            # include a element
            subset.append(candidates[i])
            dfs(i + 1, target - candidates[i], subset)
            subset.pop()

            # do not include a element
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, target, subset)

        dfs(0, target, [])
        return result


a = Solution()
candidates = [2,5,2,1,2]
target = 5
result = a.combinationSum2(candidates, target)
print(result)
