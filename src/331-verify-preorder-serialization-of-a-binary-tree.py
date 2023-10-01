class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        def hasSingleHash(stack):
            return len(stack) == 1 and stack[0] == "#"

        if preorder == "#":
            return True
        preorderStack = preorder.split(',')
        stack = []

        for v in preorderStack:
            if hasSingleHash(stack):
                return False
            stack.append(v)

            while len(stack) >= 2 and stack[-1] == "#" and stack[-2] == "#":
                if len(stack) == 2:
                    return False
                stack = stack[:-3]
                stack.append("#")
        return hasSingleHash(stack)
