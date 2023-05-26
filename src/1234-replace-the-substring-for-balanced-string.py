from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        l = 0
        res = 1e9
        criteria = len(s) / 4

        # Q,W,E,R 중에 어떤 key 가 criteria 를 오버했는 지 알아야 함
        excess = {}
        for key in counter:
            if counter[key] > criteria:
                excess[key] = counter[key] - criteria
        if not excess:
            return 0
        for r in range(len(s)):
            if s[r] in excess:
                excess[s[r]] -= 1

            while all(val <= 0 for val in excess.values()):
                res = min(res, r - l + 1)

                if s[l] in excess:
                    excess[s[l]] += 1
                l += 1

        return res
