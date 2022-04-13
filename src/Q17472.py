from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
MAP = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def isEdge(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and MAP[nx][ny] == 0:
            return True
    return False


def makeBridge(nx, ny, d, nowBridge):
    bridgeArrayList = [[] for _ in range(totalIslandCnt + 1)]
    connectedBridge = 0
    cnt = 0  # 다리 길이
    while 0 <= nx < n and 0 <= ny < m:
        if MAP[nx][ny] != 0:
            connectedBridge = MAP[nx][ny]
        nx += dx[d]
        ny += dy[d]
        cnt += 1
    if cnt < 2 or connectedBridge == 0:
        return
    bridgeArrayList[nowBridge].append(connectedBridge)


def dfs(x, y):
    if not isEdge(x, y):
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and MAP[nx][ny] == 0:
            makeBridge(nx, ny, i)


def makeMap(i, j, num):
    q = deque()
    q.append((i, j))
    MAP[i][j] = num
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and MAP[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                MAP[nx][ny] = num
                visited[nx][ny] = True


totalIslandCnt = 1
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if MAP[i][j] == 1 and visited[i][j] == False:
            makeMap(i, j, totalIslandCnt)
            totalIslandCnt += 1

for i in range(n):
    for j in range(m):
        if MAP[i][j] != 0:
            dfs(i, j)
