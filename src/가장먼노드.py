from collections import deque, defaultdict


def solution(n, edge):
    answer = 0
    connectin = defaultdict(list)

    for v1, v2 in edge:
        connectin[v1].append(v2)
        connectin[v2].append(v1)

    q = deque([1])

    visit = set()
    while q:
        cnt = 0
        for _ in range(len(q)):
            v1 = q.popleft()
            if v1 not in visit:
                visit.add(v1)
                cnt += 1
                for v2 in connectin[v1]:
                    q.append(v2)
        answer = cnt if cnt != 0 else answer

    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, edge))
