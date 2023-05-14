from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        cntr, n = Counter(s1), len(s1)
        for r in range(len(s2)):
            cntr[s2[r]] -= 1
            if r >= n:
                cntr[s2[r - n]] += 1
            if all([cntr[i] == 0 for i in cntr]):
                return True
        return False
