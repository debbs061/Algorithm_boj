from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s) # 리스트는 키가 될 수 없으니까 튜플로 변경

        return res.values()


