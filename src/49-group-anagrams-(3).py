from typing import List
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for ch in str:
                count[ord(ch) - ord("a")] += 1
            res[tuple(count)].append(str)

        return res.values()

