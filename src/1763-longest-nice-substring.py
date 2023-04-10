class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return ""
        char_set = set(s)
        for idx, c in enumerate(s):
            if c.swapcase() not in char_set:
                left_sub = self.longestNiceSubstring(s[:idx])
                right_sub = self.longestNiceSubstring(s[idx + 1:])
                return max(left_sub, right_sub, key=len)
        return s
