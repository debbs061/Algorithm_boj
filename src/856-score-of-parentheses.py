class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == ")":
                num = 0
                while stack[-1] != "(":
                    num += stack.pop()
                stack.pop()
                if num == 0:
                    stack.append(1)
                else:
                    stack.append(num * 2)
            else:
                stack.append("(")
        return sum(stack)
