from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alpha = {}
        for i in range(len(s)):
            alpha[s[i]] = i

        res = []
        lastIdx = alpha[s[0]]
        cnt = 0
        for i in range(len(s)):
            ch = s[i]
            cnt += 1
            if i == lastIdx:
                res.append(cnt)
                # 초기화 필요
                cnt = 0
                lastIdx = alpha[s[i + 1]] if i + 1 < len(s) else -1
            elif alpha[ch] > lastIdx:
                # lastIdx 갱신 여부
                lastIdx = alpha[ch]

        return res


s = "ababcbacadefegdehijhklij"
a = Solution()
print(a.partitionLabels(s))

