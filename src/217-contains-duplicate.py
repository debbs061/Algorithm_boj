class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        inputNums = set()

        for i in (nums):
            if i in inputNums:
                return True
            inputNums.add(i)

        return False
