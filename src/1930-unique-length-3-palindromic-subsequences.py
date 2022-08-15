import collections


class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        # length 3
        # only lower case
        res, left = set(), set()
        right = collections.Counter(s)

        for i in range(len(s)):  # consider i as a middle
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])

            # check outside is same
            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in right:
                    res.add((s[i], c))

            left.add(s[i])
        return len(res)
