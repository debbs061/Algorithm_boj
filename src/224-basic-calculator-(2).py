class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        stack = []
        num, sign = 0, '+'

        def update(op, v):
            if op == "+":
                stack.append(v)
            else:
                stack.append(-v)

        while i < len(s):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            elif s[i] in '+-':
                update(sign, num)
                sign, num = s[i], 0
            elif s[i] == "(":
                num, j = self.calculate(s[i + 1:])
                i = i + j
            elif s[i] == ")":
                update(sign, num)
                return sum(stack), i + 1
            i += 1
        update(sign, num)
        return sum(stack)
