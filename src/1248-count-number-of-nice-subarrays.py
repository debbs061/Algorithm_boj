from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # return the number of subarray which k odds on it

        def at_most_k_odds(nums, k):
            l = count = 0
            for r, n in enumerate(nums):
                k -= n % 2
                while k < 0:
                    k += nums[l] % 2
                    l += 1
                count += r - l + 1
            return count

        return at_most_k_odds(nums, k) - at_most_k_odds(nums, k - 1)
