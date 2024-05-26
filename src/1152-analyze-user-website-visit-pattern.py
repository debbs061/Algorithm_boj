from typing import List
from collections import defaultdict, Counter
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        pattern = Counter()
        userToSites = defaultdict(list)

        sorted_list = sorted(list(zip(username, timestamp, website)), key=lambda x: (x[0], x[1]))

        for u, t, w in sorted_list:
            userToSites[u].append(w)

        for websites in userToSites.values():
            pattern.update(Counter(set(combinations(websites, 3))))

        return max(sorted(pattern), key=pattern.get)
