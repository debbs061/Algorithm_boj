class Solution(object):
    def longestPalindromeSubseq(self, s):

        def isPalindrome(str):
            maxLen = 0
            for i in range(len(str)):
                l, r = i, i
                while l >= 0 and r < len(str) and str[l] == str[r]:
                    maxLen = max(maxLen, r - l + 1)
                    l -= 1
                    r += 1

                l, r = i, i + 1
                while l >= 0 and r < len(str) and str[l] == str[r]:
                    maxLen = max(maxLen, r - l + 1)
                    l -= 1
                    r += 1
            return maxLen

            # recursively make all the subsequences

        subseq = set()
        subseq.add("")

        def makeStr(subseq):
            for i in range(len(s)):
                newSubseq = set()
                for sub in subseq:
                    newSubseq.add(sub)
                    newSubseq.add(sub + s[i])
                subseq = newSubseq

            maxLen = 1
            for sub in subseq:
                subLen = isPalindrome(sub)
                maxLen = max(maxLen, subLen)
            return maxLen

        return makeStr(subseq)
