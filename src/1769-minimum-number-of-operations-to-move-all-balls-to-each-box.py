from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)
        res = [0 for _ in range(n)]
        for i in range(1, n):
            if boxes[i - 1] == "1":
                leftCount += 1
            leftCost += leftCount
            res[i] = leftCost

        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == "1":
                rightCount += 1
            rightCost += rightCount
            res[i] += rightCost
        return res
