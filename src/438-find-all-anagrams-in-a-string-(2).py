from typing import List
from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        tar, cur = Counter(), Counter()
        l = 0

        for idx, ch in enumerate(p):
            tar[ch] += 1
            cur[s[idx]] += 1

        res = [0] if tar == cur else []

        for r in range(len(p), len(s)):
            cur[s[r]] += 1
            cur[s[l]] -= 1
            if cur[s[l]] == 0:
                del cur[s[l]]
            l += 1

            if tar == cur:
                res.append(l)

        return res
