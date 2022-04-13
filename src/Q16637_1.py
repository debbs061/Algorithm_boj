from sys import stdin


def calculate(sub_total, x, op):
    if op == '+':
        sub_total += x
    elif op == '*':
        sub_total *= x
    elif op == '-':
        sub_total -= x
    return sub_total


def dfs(idx, sub_total):
    global answer
    if idx >= len(data):
        answer = max(answer, sub_total)
        return

    if idx == 0:
        op = '+'
    else:
        op = data[idx - 1]

    # 괄호 넣기
    if idx + 2 < len(data):
        dfs(idx + 4, calculate(sub_total, calculate(int(data[idx]), int(data[idx + 2]), data[idx + 1]), op))

    # 괄호 안 넣기
    dfs(idx + 2, calculate(sub_total, int(data[idx]), op))


n = int(stdin.readline())
data = stdin.readline().rstrip()
answer = -1e9
dfs(0, 0)
print(answer)
