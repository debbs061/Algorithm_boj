import sys
from collections import deque

input = sys.stdin.readline()
n, k = map(int, input.split())
visited = [False] * 100001
time = 0
cases = 0

q = deque()
visited[n] = True
q.append((n, 0))

while q:
    x, cnt = q.popleft()

    for next in (x * 2, x + 1, x - 1):
        if 0 <= next <= 100000:
            if not visited[next]:
                visited[next] = True
                q.append((next, cnt + 1))
            else:
                if next == k:
                    if time != 0:
                        if time == cnt:
                            cases += 1
                    else:
                        time = cnt
                        cases += 1

print(time)
print(cases)
