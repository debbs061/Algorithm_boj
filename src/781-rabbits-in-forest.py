from typing import List
from collections import defaultdict, Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbitNumToFreq = Counter(answers)
        res = 0

        for rabbitNum, freq in rabbitNumToFreq.items():
            maxNumInTeam = rabbitNum + 1
            TeamCnt = freq // maxNumInTeam
            remainderNum = maxNumInTeam if freq % maxNumInTeam else 0
            res += (TeamCnt * maxNumInTeam) + remainderNum

        return res
