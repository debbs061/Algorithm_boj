from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha = Counter()
        l = res = 0

        for r in range(len(s)):
            alpha[s[r]] += 1

            while (r - l + 1) - max(alpha.values()) > k:
                alpha[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
