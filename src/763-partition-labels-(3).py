import collections
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alphaMap = collections.Counter()
        for idx, val in enumerate(s):
            alphaMap[val] = idx

        res = []
        i, startIdx = 0, 0
        while i < len(s):
            lastIdx = alphaMap[s[i]]
            while i < lastIdx:
                lastIdx = max(lastIdx, alphaMap[s[i]])
                i += 1
            # partition 진행
            res.append(lastIdx - startIdx + 1)
            startIdx = i + 1
            i += 1
        return res

a = Solution()
s = "eccbbbbdec"
print(a.partitionLabels(s))
