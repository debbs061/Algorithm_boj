from typing import List


# my solution - binary search 조합
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(s, e, target, excludeIdx):
            if s > e:
                return -1
            m = (s + e) // 2
            if numbers[m] == target:
                if m == excludeIdx:
                    if m - 1 < len(numbers) and numbers[m + 1] == target:
                        return m + 1
                    elif m - 1 >= 0 and numbers[m - 1] == target:
                        return m - 1
                    else:
                        return -1
                return m
            elif numbers[m] < target:
                return binarySearch(m + 1, e, target, excludeIdx)
            else:
                return binarySearch(s, m - 1, target, excludeIdx)

        for idx, num in enumerate(numbers):
            otherNum = target - num
            otherIdx = binarySearch(0, len(numbers) - 1, otherNum, idx)
            if otherIdx != -1:
                return [idx + 1, otherIdx + 1]
