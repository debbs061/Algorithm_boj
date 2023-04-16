class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a', 'e', 'i', 'o', 'u'}

        res = l = cnt = 0
        for r in range(len(s)):
            if s[r] in vowels:
                cnt += 1
            if r - l + 1 >= k:
                res = max(res, cnt)
                if s[l] in vowels:
                    cnt -= 1
                l += 1

        return res
