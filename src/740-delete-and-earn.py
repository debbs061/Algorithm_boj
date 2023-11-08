from typing import List
from collections import defaultdict, Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cache = defaultdict(int)  # cache[i] = i번째부터 끝까지 해서 얻을 수 있는 max point
        numsFreq = Counter(nums)
        nums = sorted(numsFreq.keys())

        def recurse(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            # pick i and earn the money
            nextIdx = i + 2 if nums[i] + 1 in numsFreq else i + 1
            earn = (nums[i] * numsFreq[nums[i]]) + recurse(nextIdx)

            # not pick i
            notEarn = recurse(i + 1)

            cache[i] = max(earn, notEarn)
            return cache[i]

        return recurse(0)
