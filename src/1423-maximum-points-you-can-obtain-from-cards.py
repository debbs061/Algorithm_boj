from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        untakenPointsCnt = len(cardPoints) - k
        untakenPointsSum = l = 0
        minUntakenPointsSum = 1e9
        for r in range(len(cardPoints)):
            untakenPointsSum += cardPoints[r]
            if r - l + 1 == untakenPointsCnt:
                minUntakenPointsSum = min(minUntakenPointsSum, untakenPointsSum)
                untakenPointsSum -= cardPoints[l]
                l += 1
        return sum(cardPoints) - minUntakenPointsSum
