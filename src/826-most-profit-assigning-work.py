from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()

        res, curMaxProfit, curIdx = 0, 0, 0
        for skill in worker:
            while curIdx < len(difficulty) and jobs[curIdx][0] <= skill:
                curMaxProfit = max(curMaxProfit, jobs[curIdx][1])
                curIdx += 1
            res += curMaxProfit
        return res
