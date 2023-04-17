from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = currGrumpySum = currSatisfiedSum = 0
        maxGrumpySum = -1e9
        for r in range(len(grumpy)):
            if grumpy[r] == 1:
                currGrumpySum += customers[r]
            else:
                currSatisfiedSum += customers[r]
            if r - l + 1 == minutes:
                if currGrumpySum > maxGrumpySum:
                    maxGrumpySum = currGrumpySum
                if grumpy[l] == 1:
                    currGrumpySum -= customers[l]
                l += 1
        return currSatisfiedSum + maxGrumpySum
