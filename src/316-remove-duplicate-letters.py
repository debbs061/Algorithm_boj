from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        increasingStack = []
        alphaMap = Counter()
        alphaSet = set()

        for ch in s:
            alphaMap[ch] += 1

        for ch in s:
            n = ch
            if n not in alphaSet:
                while increasingStack and increasingStack[-1] > n and alphaMap[increasingStack[-1]] > 0:
                    n2 = increasingStack.pop()
                    alphaSet.remove(n2)
                alphaSet.add(n)
                increasingStack.append(n)
            alphaMap[n] -= 1
        return "".join([n for n in increasingStack])
