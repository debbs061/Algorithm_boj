import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    global result
    q = deque()
    visit[a][b] = True
    q.append((a, b, 0))
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 'L' and not visit[nx][ny]:
                result = max(result, cnt + 1)
                visit[nx][ny] = True
                q.append((nx, ny, cnt + 1))


input = sys.stdin.readline
n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(input()))

result = -1e9
for i in range(n):
    for j in range(m):
        if data[i][j] == 'L':
            visit = [[False] * m for _ in range(n)]
            bfs(i, j)

print(result)
