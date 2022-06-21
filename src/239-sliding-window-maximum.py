import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        output = []
        q = collections.deque()  # saves index
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r - l + 1) == k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
