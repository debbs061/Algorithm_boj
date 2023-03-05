from typing import List


class Solution:
    # sol2. two pointers
    # time - o(nlogn + mlogm) , memory - o(n)
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     l, r = 0, 0
    #     res = []
    #     nums1.sort()
    #     nums2.sort()
    #     while l < len(nums1) and r < len(nums2):
    #         if nums1[l] == nums2[r]:
    #             res.append(nums1[l])
    #             l += 1
    #             r += 1
    #         elif nums1[l] < nums2[r]:
    #             l += 1
    #         else:
    #             r += 1
    #
    #     return res

    # sol1. use hash map
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time - o(n+m) , memory - o(n)

        inter = {}
        for n in nums1:
            inter[n] = inter.get(n, 0) + 1

        res = []
        for n in nums2:
            if n in inter and inter[n] > 0:
                res.append(n)
                inter[n] -= 1

        return res
