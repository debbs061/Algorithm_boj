class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = []
        for c in s:
            if c.isalpha() or c.isnumeric():
                newStr.append(c.lower())
        print(newStr)
        l, r = 0, len(newStr) - 1
        while l < r:
            if newStr[l] != newStr[r]:
                return False
            l += 1
            r -= 1
        return True
