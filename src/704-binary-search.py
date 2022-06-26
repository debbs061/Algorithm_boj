class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums, start, end, target):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(nums, start, mid - 1, target)
        else:
            return self.binarySearch(nums, mid + 1, end, target)


a = Solution()
a.search([-1, 0, 3, 5, 9, 12], 9)
