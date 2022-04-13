from collections import deque
m,n = map(int, input().split())
data = []
visited = [[False] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if data[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    visited[nx][ny] = True
                    q.appendleft((nx, ny))
                else:  # 벽 부수는 경우
                    dist[nx][ny] = dist[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx, ny))


dist[0][0] = 0
visited[0][0] = True
bfs(0, 0)
print(dist[n-1][m-1])
