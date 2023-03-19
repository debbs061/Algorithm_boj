class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for idx, ch in enumerate(s):
            if ch == "]":
                tmp = ""
                while stack[-1] != "[":
                    tmp = stack.pop() + tmp
                stack.pop()  # pop "["

                repeat = ""
                while stack and stack[-1].isdigit():
                    repeat = stack.pop() + repeat

                stack.append(int(repeat) * tmp)

            else:
                stack.append(ch)

        return "".join(stack)
