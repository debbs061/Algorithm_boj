class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(i, cur, total):
            if i >= len(candidates) or total > target:
                return
            if total == target:
                res.append(cur.copy())  # shallow copy. (이 이후의 연산들이 cur 에 영향을 줄거기 때문에 복사본 자체를 넣어준다)
                return

            # to include
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # not to include
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
