class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = r = curCost = 0

        for r in range(len(s)):
            curCost += abs(ord(s[r]) - ord(t[r]))
            if curCost > maxCost:
                curCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

        return r - l + 1
