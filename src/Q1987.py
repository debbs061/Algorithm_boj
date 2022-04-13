import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
check = [False] * 26

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
maxi = 0


def dfs(x, y, cnt):
    global maxi
    maxi = max(cnt, maxi)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and check[ord(arr[nx][ny]) - 65] == False:
            check[ord(arr[nx][ny]) - 65] = 1
            nCnt = cnt + 1
            dfs(nx, ny, nCnt)
            check[ord(arr[nx][ny]) - 65] = 0


check[ord(arr[0][0]) - 65] = 1
dfs(0, 0, 1)
print(maxi)
