import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            firstVal = minH[0]
            for i in range(firstVal, firstVal + groupSize):
                if i not in count:
                    return False

                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
