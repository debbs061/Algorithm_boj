class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def doBackspace(input):
            stack = []
            for v in input:
                if v == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(v)
            return "".join(stack)

        return doBackspace(s) == doBackspace(t)
