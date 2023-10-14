from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        # 왼쪽에서 시작하여, 증가하는 최대 부분 배열의 길이를 찾음
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # 모든 배열이 증가하는 경우
        if left == n - 1:
            return 0

        # 오른쪽에서 시작하여, 증가하는 최대 부분 배열의 길이를 찾음
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # 전체 배열을 고려하여, 최소 제거 길이를 찾음
        # n-left-1 = 오른쪽에서 시작하는 배열을 제거하는 경우
        # right = 왼쪽에서 시작하는 배열을 제거하는 경우
        result = min(n - left - 1, right)

        # 2. 양쪽에서 일부분을 유지하며, 중간 부분을 제거하는 경우
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                # i: 왼쪽 부분 배열의 마지막 인덱스, j: 오른쪽 부분 배열의 시작 인덱스
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result
