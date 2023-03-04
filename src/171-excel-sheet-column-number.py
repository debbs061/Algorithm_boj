class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        pos, ans = 0, 0
        for i, ch in enumerate(reversed(columnTitle)):
            d = ord(ch) - 64
            ans += (26 ** pos) * d
            pos += 1

        return ans
