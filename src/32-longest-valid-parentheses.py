class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        max_len = 0
        last_invalid = -1  # 마지막으로 유효하지 않은 괄호의 위치를 기억합니다.

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack:  # 스택이 비어있지 않을 때
                    stack.pop()
                    if not stack:  # 모든 괄호가 매치되었을 때
                        max_len = max(max_len, i - last_invalid)
                    else:  # 일부 괄호만 매치되었을 때
                        max_len = max(max_len, i - stack[-1])
                else:  # 스택이 비어있을 때
                    last_invalid = i

        return max_len
