from collections import deque


def solution(maps):
    answer = 0
    q = deque()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ROWS, COLS = len(maps), len(maps[0])

    q.append((0, 0, 1))
    visit = set()
    while q:
        x, y, cnt = q.popleft()
        if (x, y) in visit:
            continue
        if x == ROWS - 1 and y == COLS - 1:
            return cnt
        visit.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and maps[nx][ny] == 1:
                q.append((nx, ny, cnt + 1))

    return -1
