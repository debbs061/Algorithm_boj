from typing import List
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        numToFreq = Counter(nums)

        for i in sorted(numToFreq):  # i번째를 시작으로 하는 set 검사
            if numToFreq[i] > 0:
                for j in range(k)[::-1]:  # consecutive 숫자들 처리
                    numToFreq[i + j] -= numToFreq[i]
                    if numToFreq[i + j] < 0:
                        return False
        return True
