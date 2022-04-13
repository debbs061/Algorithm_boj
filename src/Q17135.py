from sys import stdin


def moveDownSide():


input = stdin.readline()
n, m, d = map(int, input.split())
data = [list(map(int, input.split())) for _ in range(n)]
answer = -1e9
# 서 북 동 남
dx = [0, -1, 0, 0]
dy = [-1, 0, 1, 1]

# start
for _ in range(n):
    for _ in range(3):


    moveDownSide()

# end
print(answer)
