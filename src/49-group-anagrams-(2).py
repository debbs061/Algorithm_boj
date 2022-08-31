import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for str in strs:
            cnt = [0] * 26
            for c in str:
                num = ord(c) - ord('a')
                cnt[num] += 1
            result[tuple(cnt)].append(str)

        return result.values()
