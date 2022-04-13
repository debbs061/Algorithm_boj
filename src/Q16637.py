from math import inf
from sys import stdin


def calculate(a, b, op):
    if op == '+':
        a += b
    elif op == '-':
        a -= b
    elif op == '*':
        a *= b
    return a


def dfs(idx, sub_total):
    global answer

    if idx >= n:
        answer = max(answer, sub_total)
        return

    if idx == 0:
        op = '+'
    else:  # 첫번째 수가 아닌 경우, 자기 앞의 연산자를 op 에다가 저장
        op = str[idx - 1]

    # 괄호 묶는 경우
    if idx + 2 < n:
        bracket = calculate(int(str[idx]), int(str[idx + 2]), str[idx + 1])
        dfs(idx + 4, calculate(sub_total, bracket, op))

    dfs(idx + 2, calculate(sub_total, int(str[idx]), op))


n = int(stdin.readline())
str = stdin.readline().rstrip()
answer = -inf

dfs(0, 0)
print(answer)
