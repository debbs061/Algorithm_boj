n = int(input())
ugly = [0] * n  # 못생긴 수를 담기 위한 테이블 (1차원 dp 테이블)
ugly[0] = 1  # 첫 번째 못생긴 수는 1

i2 = i3 = i5 = 0  # 2배, 3배, 5배를 위한 인덱스
next2, next3, next5 = 2, 3, 5  # 처음에 곱셈값을 초기화

# 1부터 n까지의 못생긴 수 찾기 (1<=n<=2000)
for l in range(1, n):
    ugly[l] = min(next2, next3, next5)  # 가능한 곱셈 결과 중에서 가장 작은 수를 먼저 선택
    # 가능한 못생긴 수를 앞에서부터 찾아 나간다.
    # 그 못생긴 수에 2,3,5 를 곱해준 수도 못생긴 수이다.
    # 수는 오름차순으로 ugly 배열에 넣어져야하므로 인덱스로 따로 관리한다.
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

# n번째 못생긴 수를 출력
print(ugly[n - 1])
