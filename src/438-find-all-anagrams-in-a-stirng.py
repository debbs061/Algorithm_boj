from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        have = defaultdict(int)
        match = defaultdict(int)

        for idx, ch in enumerate(p):
            match[ch] += 1
            have[s[idx]] += 1

        result = [0] if match == have else []
        l = 0
        for r in range(len(p), len(s)):
            have[s[r]] += 1
            have[s[l]] -= 1
            if have[s[l]] == 0:
                del have[s[l]]
            l += 1

            if have == match:
                result.append(l)

        return result
