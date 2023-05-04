from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        xClosestIdx = 1e9

        # Time - O(n)
        for i in range(len(arr) - 1):
            if i + 1 < len(arr) and arr[i] <= x <= arr[i + 1]:
                xClosestIdx = i + 1 if abs(arr[i] - x) > abs(arr[i + 1] - x) else i
                break

        if xClosestIdx == 1e9:
            if x <= arr[0]:
                xClosestIdx = 0
            if x >= arr[len(arr) - 1]:
                xClosestIdx = len(arr) - 1

        res.append(arr[xClosestIdx])
        k -= 1
        l, r = xClosestIdx - 1, xClosestIdx + 1
        while k > 0:
            if l >= 0 and r < len(arr):
                if abs(arr[l] - x) > abs(arr[r] - x):
                    res.append(arr[r])
                    r += 1
                else:
                    res.append(arr[l])
                    l -= 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < len(arr):
                res.append(arr[r])
                r += 1
            else:
                break
            k -= 1

        return sorted(res)
