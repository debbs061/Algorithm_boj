from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k])

        # initialize
        if curSum / k >= threshold:
            res += 1
        curSum -= arr[0]
        l = 1

        for r in range(k, len(arr)):
            curSum += arr[r]
            # average
            if curSum / k >= threshold:
                res += 1
            curSum -= arr[l]
            l += 1
        return res
