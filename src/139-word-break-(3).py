from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i >= len(s):
                return True

            for word in wordDict:
                if s[i:i + len(word)] == word:
                    if dfs(i + len(word)):
                        cache[i] = True
                        return True

            cache[i] = False
            return cache[i]

        dfs(0)
        return cache[0]
