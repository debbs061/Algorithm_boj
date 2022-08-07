class Solution(object):
    def canPartition(self, nums):
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        subSum = set()
        subSum.add(0)

        for i in range(len(nums)):
            tmpSubSum = set()
            for t in subSum:
                if nums[i] + t == target:
                    return True
                tmpSubSum.add(t + nums[i])
                tmpSubSum.add(t)
            subSum = tmpSubSum

        return False
