from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashMap = defaultdict(list)
        res = []
        for i in range(len(groupSizes)):
            hashMap[groupSizes[i]].append(i)
            if len(hashMap[groupSizes[i]]) == groupSizes[i]:
                res.append(hashMap[groupSizes[i]])
                hashMap[groupSizes[i]] = []

        return res
