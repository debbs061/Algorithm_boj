from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    # return the number of good subarrays (exactly K unique number)
    def atMostK(self, nums, k):
        count = Counter()
        l = res = 0
        for r in range(len(nums)):
            if count[nums[r]] == 0:
                k -= 1
            count[nums[r]] += 1
            while k < 0:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    k += 1
                l += 1
            res += r - l + 1
        return res
