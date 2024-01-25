from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        res = 0
        properties.sort(key=lambda x: (x[0], -x[1]))

        for i in range(len(properties) - 1):
            for j in range(i + 1, len(properties)):
                if properties[i][0] < properties[j][0] and properties[i][1] < properties[j][1]:
                    res += 1
                    i = j - 1
                    break
        return res


a = Solution()
properties = [[1, 1], [2, 1], [2, 2], [1, 2]]
print(a.numberOfWeakCharacters(properties))
