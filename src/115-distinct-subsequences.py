class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        # s = "rabbbit" , t = "rabbit"
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            cnt = dfs(i + 1, j)
            if s[i] == t[j]:
                cnt += dfs(i + 1, j + 1)

            dp[(i, j)] = cnt

            return dp[(i, j)]

        return dfs(0, 0)
