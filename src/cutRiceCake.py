import sys

# 내 풀이. 이진탐색으로 풀음
def cutDduck(cuttingHeight):
    sum = 0
    for i in data:
        if i > cuttingHeight:
            i -= cuttingHeight
            sum += i
    return sum


def binary_search(start, end, target):
    global answer
    if start >= end:
        return
    mid = (start + end) // 2
    sumDduck = cutDduck(mid)
    if sumDduck == target:
        answer = mid
        return
    elif sumDduck > target:
        binary_search(mid + 1, end, target)
    else:
        binary_search(start, mid - 1, target)


input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
answer = 0
binary_search(0, data[0], m)
print(answer)
