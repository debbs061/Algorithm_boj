from typing import List
from collections import Counter


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cnt = Counter()

        for r in range(len(nums)):
            if nums[r] in cnt:
                prevIdx = cnt[nums[r]]
                if abs(prevIdx - r) <= k:
                    return True
            cnt[nums[r]] = r

        return False
