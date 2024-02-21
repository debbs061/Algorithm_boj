from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordToFreq = Counter(words)
        length = 0
        for word in words:
            # 동일 char 인 경우
            if word == word[::-1]:
                if wordToFreq[word] >= 2:
                    wordToFreq[word] -= 2
                    length += 4
            # 동일 char 아닌 경우
            else:
                if wordToFreq[word] > 0:
                    reversedWord = word[::-1]
                    if wordToFreq[reversedWord] > 0:
                        wordToFreq[reversedWord] -= 1
                        wordToFreq[word] -= 1
                        length += 4

        for k, v in wordToFreq.items():
            if k == k[::-1] and v > 0:
                length += 2
                break
        return length
