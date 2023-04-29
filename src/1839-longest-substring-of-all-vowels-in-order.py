from collections import Counter


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = set()
        l = res = 0
        for r in range(len(word)):
            if r - 1 >= 0 and word[r - 1] > word[r]:
                vowels = set()
                l = r
            vowels.add(word[r])

            if len(vowels) == 5:
                res = max(res, r - l + 1)
        return res
