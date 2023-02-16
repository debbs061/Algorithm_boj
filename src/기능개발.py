import math


def solution(progresses, speeds):
    answer = []

    # 남은 일수 계산
    remain_days = []
    for i in range(len(progresses)):
        remain_days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    i, count = 1, 1
    prev_day = remain_days[0]
    while i < len(remain_days):
        if prev_day < remain_days[i]:
            answer.append(count)
            prev_day = remain_days[i]
            count = 1
        else:
            count += 1
        i += 1

    if count > 0:
        answer.append(count)
    return answer
