import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j, num, map):
    color = map[i][j]
    q = deque()
    q.append((i, j))
    visit[i][j] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and map[nx][ny] == color:
                q.append((nx, ny))
                visit[nx][ny] = num


n = int(input())
normal = [list(input().rstrip()) for _ in range(n)]
unNormal = [[''] * n for _ in range(n)]

# 적록색약용 맵 생성
for i in range(n):
    for j in range(n):
        if normal[i][j] == 'R':
            unNormal[i][j] = 'G'
        else:
            unNormal[i][j] = normal[i][j]

# 적록색약이 아닌 사람이 보는 경우
answer = []
visit = [[0] * n for _ in range(n)]
normalNum = 0
unNormalNum = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            normalNum += 1
            bfs(i, j, normalNum, normal)
answer.append(normalNum)

# 적록색약인 사람이 보는 경우
visit = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            unNormalNum += 1
            bfs(i, j, unNormalNum, unNormal)
answer.append(unNormalNum)

for i in range(len(answer)):
    print(answer[i], end=' ')
