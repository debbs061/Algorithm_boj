from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        # return the number of subarrays at most k element
        def getNumOfAtMostKelement(nums, atMost):
            count, r, l = defaultdict(int), 0, 0
            res = 0
            for r in range(len(nums)):
                count[nums[r]] += 1
                while len(count) > atMost:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                res += r - l + 1
            return res

        return getNumOfAtMostKelement(nums, k) - getNumOfAtMostKelement(nums, k - 1)


nums = [1, 2, 1, 2, 3]
k = 2
a = Solution()
print(a.subarraysWithKDistinct(nums, k))
