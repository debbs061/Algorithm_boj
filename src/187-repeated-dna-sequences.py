from typing import List
from collections import Counter, deque


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        l = 0
        res = set()
        seen = set()

        for r in range(len(s)):
            if r >= 9:
                curStr = s[l:r + 1]
                if curStr in seen:
                    res.add(curStr)
                else:
                    seen.add(curStr)
                l += 1

        return list(res)
