from typing import List
from collections import Counter


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = Counter()  # {num : length}
        res = 0
        for n in arr:
            dp[n] = dp[n - difference] + 1
            res = max(res, dp[n])
        return res
