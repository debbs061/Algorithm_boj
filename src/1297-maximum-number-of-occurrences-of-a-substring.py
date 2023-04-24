from collections import Counter


class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        count = Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1))
        return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])

    # def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    #     l = 0
    #     letterMap = Counter()
    #     occurrence = Counter()
    #     for r in range(len(s)):
    #         letterMap[s[r]] += 1
    #
    #         # if met the condition ...
    #         while len(letterMap) > maxLetters:
    #             letterMap[s[l]] -= 1
    #             if letterMap[s[l]] == 0:
    #                 del letterMap[s[l]]
    #             l += 1
    #
    #         while maxSize < r - l + 1:
    #             letterMap[s[l]] -= 1
    #             if letterMap[s[l]] == 0:
    #                 del letterMap[s[l]]
    #             l += 1
    #
    #         if minSize <= r - l + 1 <= maxSize:
    #             occurrence[s[l:r + 1]] += 1
    #
    #     return max(occurrence.values())
