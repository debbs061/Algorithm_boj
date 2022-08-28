class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1

            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0

# sol 2. dp + memoization
# cache = {}  # (i, left) -> T/F
#
# def dfs(i, left):
#     if i == len(s):
#         if left == 0:
#             return True
#         return False
#
#     if left < 0:
#         return False
#
#     if (i, left) in cache:
#         return cache[(i, left)]
#
#     if s[i] == "(":
#         cache[(i, left)] = dfs(i + 1, left + 1)
#
#     elif s[i] == ")":
#         cache[(i, left)] = dfs(i + 1, left - 1)
#
#     else:
#         cache[(i, left)] = dfs(i + 1, left - 1) or dfs(i + 1, left + 1) or dfs(i + 1, left)
#
#     return cache[(i, left)]
#
# dfs(0, 0)
# return cache[(0, 0)]
