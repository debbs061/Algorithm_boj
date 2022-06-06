class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(num) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target: # to speed up (optimization)
                    return True
                nextDP.add(t + nums[i])  # 선택하고
                nextDP.add(t)  # 선택 안 하고
            dp = nextDP
        return True if target in dp else False
