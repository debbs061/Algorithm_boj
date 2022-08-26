from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1

        return res

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#
#         # i+jump >= N -1: success
#         N = len(nums)
#         d = [1e9] * N
#         d[N-1] = 0
#         for i in range(N-2,-1,-1):
#             jump = nums[i]
#             if i+jump >= N -1:
#                     d[i] = 1
#                     continue
#
#             while jump != 0:
#                 if i+jump >= N -1:
#                     d[i] = 1
#                     break
#                 d[i] = min(d[i], d[i+jump] + 1)
#                 jump -= 1
#
#         return d[0]
