from collections import Counter


class Solution:
    def isMatch(self, sCounter, tCounter):
        for ch in tCounter:
            if tCounter[ch] > sCounter[ch]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        sCounter = Counter()
        l = 0
        res = 1e9
        lIdx, rIdx = 0, 0
        for r in range(len(s)):
            sCounter[s[r]] += 1
            while self.isMatch(sCounter, tCounter):
                if r - l + 1 < res:
                    res = r - l + 1
                    lIdx, rIdx = l, r
                sCounter[s[l]] -= 1
                if sCounter[s[l]] == 0:
                    del sCounter[s[l]]
                l += 1

        return s[lIdx:rIdx + 1] if res != 1e9 else ""
