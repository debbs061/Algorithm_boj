from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find the intersection in a cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # find the beginning of a cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
