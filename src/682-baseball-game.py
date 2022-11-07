from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "+":
                num1, num2 = stack[-1], stack[-2]
                stack.append(num1 + num2)
            elif o == 'D':
                num1 = stack[-1]
                stack.append(num1 * 2)
            elif o == 'C':
                stack.pop()
            else:
                stack.append(int(o))

        return sum(stack)
