from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(leftBias):
            i = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    i = m
                    if leftBias:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return i

        return [binarySearch(True), binarySearch(False)]

        # My solution
#
# res = [-1, -1]
# l, r = 0, len(nums) - 1
# while l <= r:
#     m = (l + r) // 2
#     if nums[m] == target:
#         l1, l2 = m - 1, m + 1
#         t = [m, m]
#         while l1 >= l and nums[l1] == target:
#             t[0] = l1
#             l1 -= 1
#         while l2 <= r and nums[l2] == target:
#             t[1] = l2
#             l2 += 1
#         return t
#     elif nums[m] < target:
#         l = m + 1
#     else:
#         r = m - 1
#
# return res
