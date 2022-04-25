from collections import deque

def bfs(n):
    q = deque()
    q.append((n, 0))
    while q:
        x, cnt = q.popleft()
        if x == 1:
            print(cnt)
            exit()
        if x % 5 == 0 and x / 5 > 0 and not visit[x // 5]:
            newX = x / 5
            visit[newX] = True
            q.append((newX, cnt + 1))
        if x % 3 == 0 and x / 3 > 0 and not visit[x // 3]:
            newX = x / 3
            visit[newX] = True
            q.append((newX, cnt + 1))
        if x % 2 == 0 and x / 2 > 0 and not visit[x // 2]:
            newX = x / 2
            visit[newX] = True
            q.append((newX, cnt + 1))
        if x - 1 > 0 and not visit[x - 1]:
            newX = x - 1
            visit[newX] = True
            q.append((newX, cnt + 1))


n = int(input())
visit = [False] * 30001
bfs(n)
