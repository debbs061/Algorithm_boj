from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        l = 0
        longest = -float("inf")
        for r in range(len(s)):
            cnt[s[r]] += 1
            while (r - l + 1) - max(cnt.values()) > k:
                cnt[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
