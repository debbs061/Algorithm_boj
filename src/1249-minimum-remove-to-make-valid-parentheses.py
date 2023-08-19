class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openParens = 0
        stack = []
        for ch in s:
            if ch == "(":
                openParens += 1
                stack.append(ch)
            elif ch == ")":
                if openParens > 0:
                    openParens -= 1
                    stack.append(ch)
            else:
                stack.append(ch)

        newStack = []
        for i in range(len(stack) - 1, -1, -1):
            if openParens > 0 and stack[i] == "(":
                openParens -= 1
            else:
                newStack.append(stack[i])
        newStack.reverse()
        return "".join(newStack)
