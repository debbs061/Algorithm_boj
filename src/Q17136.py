# 삼성 A형 기출
from math import inf
import sys


def check(r, c, length, full):  # length = 몇 개짜리 색종이?
    for i in range(length):
        full -= sum(papers[r + i][c:c + length])  # 한 줄 계산
    if full:
        return False
    else:
        return True


def recursive(one, cnt):  # 남은 1 개수, 색종이 사용 개수
    global answer
    if not one:
        answer = min(answer, cnt)
        return
    if cnt >= answer:
        return
    if not sum(used):  # 모든 색종이를 다 썼다면
        return
    for r in range(10):
        for c in range(10):
            if papers[r][c]:
                for length in range(1, 6, 1):
                    if used[length] and r + length <= 10 and c + length <= 10:
                        if check(r, c, length, length ** 2):
                            for i in range(r, r + length):
                                for j in range(c, c + length):
                                    papers[i][j] = 0
                            used[length] -= 1
                            recursive(one - length ** 2, cnt + 1)
                            for i in range(r, r + length):
                                for j in range(c, c + length):
                                    papers[i][j] = 1
                            used[length] += 1
                return  # 1이 있는데, 그 어떤 색종이로도 채울 수 없다면 return


papers = []
used = [0] + [5] * 5  # 색종이 종류별 사용 가능한 개수를 알려주는 배열
answer = inf
one = 0
for _ in range(10):
    paper = list(map(int, sys.stdin.readline().split()))
    one += sum(paper)
    papers.append(paper)

if not one:
    print(0)
else:
    recursive(one, 0)
    print(-1) if answer == inf else print(answer)
