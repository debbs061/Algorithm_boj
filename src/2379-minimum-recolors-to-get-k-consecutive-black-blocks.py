class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        l = 0
        res = 1e9
        wCount = 0
        for r in range(len(blocks)):
            if blocks[r] == "W":
                wCount += 1
            if r - l + 1 == k:
                res = min(res, wCount)
                if blocks[l] == "W":
                    wCount -= 1
                l += 1
        return res
