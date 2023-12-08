from typing import List
from collections import Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)  # {num:count}
        res = 0
        for key in freq:
            complement = k - key
            if freq[key] == 0 or freq[complement] == 0:
                continue

            if key == complement:
                res += freq[key] // 2
            else:
                res += min(freq[key], freq[complement])
                freq[key] = 0
                freq[complement] = 0
        return res
