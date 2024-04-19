from typing import List
from collections import defaultdict


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        cache = defaultdict(int)
        k = len(days[0])

        def recurse(weekIdx, cityIdx):
            if weekIdx == k:
                return 0
            if (weekIdx, cityIdx) in cache:
                return cache[(weekIdx, cityIdx)]

            maxVac = -1e9

            # move to another city
            for otherCityIdx, canMove in enumerate(flights[cityIdx]):
                if canMove:
                    maxVac = max(recurse(weekIdx + 1, otherCityIdx) + days[otherCityIdx][weekIdx], maxVac)

            # stay
            maxVac = max(recurse(weekIdx + 1, cityIdx) + days[cityIdx][weekIdx], maxVac)
            cache[(weekIdx, cityIdx)] = maxVac
            return maxVac

        return recurse(0, 0)
