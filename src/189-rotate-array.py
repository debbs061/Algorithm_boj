from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sol1. memory - o(n)
        # res = []
        # steps = k % len(nums)
        # res.extend(nums[-steps:])
        # res.extend(nums[:len(nums) - steps])
        #
        # for idx, n in enumerate(nums):
        #     nums[idx] = res[idx]

        # sol2. sorting - memory: o(1)
        # nums.reverse()
        # steps = k % len(nums)
        # nums[:len(nums)-steps].reverse()
        # nums[-steps:].reverse()

        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        k = k % len(nums)
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
