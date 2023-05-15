from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        lenS1, lenS2 = len(s1), len(s2)
        s1Map = Counter(s1)
        s2Map = Counter(s2[:lenS1])

        for i in range(lenS1, lenS2):
            if s1Map == s2Map:
                return True
            # shrink the length
            s2Map[s2[i - lenS1]] -= 1
            if s2Map[s2[i - lenS1]] == 0:
                del s2Map[s2[i - lenS1]]
            s2Map[s2[i]] += 1

        return s1Map == s2Map
