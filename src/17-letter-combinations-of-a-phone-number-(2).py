from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        sub = []
        if digits == "":
            return []
        numToLetter = {}

        numToLetter[2] = "abc"
        numToLetter[3] = "def"
        numToLetter[4] = "ghi"
        numToLetter[5] = "jkl"
        numToLetter[6] = "mno"
        numToLetter[7] = "pqrs"
        numToLetter[8] = "tuv"
        numToLetter[9] = "wxyz"

        def dfs(i):
            if i == len(digits):
                result.append("".join(sub.copy()))
                return

            for letter in numToLetter[int(digits[i])]:
                sub.append(letter)
                dfs(i + 1)
                sub.pop()

        dfs(0)
        return result

a = Solution()
digits = "23"
print(a.letterCombinations(digits))
