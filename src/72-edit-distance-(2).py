class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]  # (i,j) 에서 시작할 때, minimum operation

        for col in range(len(word2) + 1):
            cache[len(word1)][col] = len(word2) - col

        for row in range(len(word1) + 1):
            cache[row][len(word2)] = len(word1) - row

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])

        return cache[0][0]

        # def dfs(i, j):
        #     if i == len(word1) and j == len(word2):
        #         return 0
        #
        #     if (i, j) in cache:
        #         return cache[(i, j)]
        #
        #     if word1[i] == word2[j]:
        #         cache[(i, j)] = dfs(i + 1, j + 1)
        #     else:
        #         cache[(i, j)] = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
        #
        #     return cache[(i, j)]
        #
        # return dfs(0, 0)
