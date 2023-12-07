from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        def atMostK(k):  # 합이 최대 k 인 subarray 개수
            res, l = 0, 0

            for r in range(len(nums)):
                k -= nums[r]
                while l <= r and k < 0:
                    k += nums[l]
                    l += 1
                res += r - l + 1  # r 을 끝으로 하는 합이 최대 k 인 subarray 개수
            return res

        return atMostK(k) - atMostK(k - 1)
