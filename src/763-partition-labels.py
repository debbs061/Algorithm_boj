import collections
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}  # char -> last index in s

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, endIndex = 0, 0
        for i, c in enumerate(s):
            size += 1
            endIndex = max(endIndex, lastIndex[c])
            if i == endIndex:
                res.append(size)
                size = 0
        return res
        # class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         counter = collections.defaultdict(list)  # key: "a", value: [index]
#
#         for i in range(len(s)):
#             counter[s[i]].append(i)
#
#         group = []
#         size = 0
#         i = 0
#         maxIdx = i
#         maxVal = max(counter[s[maxIdx]])
#         # time - n^2
#         while i < len(s):  # 상위 기준은 계속 a 여야함
#             if maxVal < max(counter[s[i]]):
#                 if maxVal < min(counter[s[i]]):
#                     group.append(size)
#                     size = 0
#                 maxIdx = i
#                 maxVal = max(counter[s[maxIdx]])
#                 continue
#             size += 1
#             i += 1
#
#         size = size if size > 0 else 1
#         group.append(size)
#
#         return group
