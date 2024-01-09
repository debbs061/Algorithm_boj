from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # return the max side-length. 단, 정사각형의 합이 threshold 를 넘지 않아야함
        ROWS, COLS = len(mat), len(mat[0])
        prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]  # prefix[2][2] = mat[0][0] ~ mat[1][1] 합

        for r in range(ROWS):
            for c in range(COLS):
                prefix[r + 1][c + 1] = prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c] + mat[r][c]

        def check(sideLength):  # 한 변의 길이가 sideLength 인 정사각형의 합이 threshold 를 넘지 않는 케이스가 있으면 return True
            # (r,c) 는 bottom right 범위
            for r in range(sideLength, ROWS + 1):
                for c in range(sideLength, COLS + 1):
                    if prefix[r][c] - prefix[r - sideLength][c] - prefix[r][c - sideLength] + \
                            prefix[r - sideLength][c - sideLength] <= threshold:
                        return True
            return False

        sideLength = 0  # 클수록 좋음
        l, r = 0, min(ROWS, COLS)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                sideLength = mid
                l = mid + 1
            else:
                r = mid - 1

        return sideLength
