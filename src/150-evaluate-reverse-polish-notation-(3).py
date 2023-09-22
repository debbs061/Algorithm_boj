from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in ('+', '-', '*', '/'):
                second, first = int(stack.pop()), int(stack.pop())
                if ch == '+':
                    stack.append(first + second)
                elif ch == '-':
                    stack.append(first - second)
                elif ch == '*':
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
            else:
                stack.append(ch)

        return int(stack[-1])
