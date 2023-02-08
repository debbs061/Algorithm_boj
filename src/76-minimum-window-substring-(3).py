class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sMap, tMap = {}, {}
        res, resLen = [-1, -1], float("infinity")

        for ch in t:
            tMap[ch] = 1 + tMap.get(ch, 0)  # 불변

        have, need = 0, len(tMap)

        l = 0
        for r in range(len(s)):
            sMap[s[r]] = 1 + sMap.get(s[r], 0)
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                have += 1

            while have == need:
                if resLen > r - l + 1:  # update the minimum window
                    resLen = r - l + 1
                    res = [l, r]

                removed = s[l]
                sMap[removed] -= 1

                if removed in tMap and sMap[removed] < tMap[removed]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
