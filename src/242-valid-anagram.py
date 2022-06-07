class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        array = [0] * 1000
        for i in s:
            array[ord(i)] += 1

        for i in t:
            array[ord(i)] -= 1

        for i in array:
            if i != 0:
                return False
        return True

