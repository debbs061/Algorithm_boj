import sys;

input = sys.stdin.readline


def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if idx == 1:
                    visit[nx][ny] = 1
                    dfs(r, c, idx + 1, total + arr[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                dfs(nx, ny, idx + 1, total + arr[nx][ny])
                visit[nx][ny] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [([0] * m) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(n):
    for c in range(m):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)
