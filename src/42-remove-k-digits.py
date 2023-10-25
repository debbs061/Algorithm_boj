class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # increasing stack (not strict)
        for i in range(len(num)):
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while k > 0 and stack:
            k -= 1
            stack.pop()

        tmp = "".join(stack)

        # 선행 0을 수동으로 제거
        idx = 0
        while idx < len(tmp) and tmp[idx] == "0":
            idx += 1

        return tmp[idx:] or "0"
