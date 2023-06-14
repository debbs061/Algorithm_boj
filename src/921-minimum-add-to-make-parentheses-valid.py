class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 2 and stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()

        return len(stack)
