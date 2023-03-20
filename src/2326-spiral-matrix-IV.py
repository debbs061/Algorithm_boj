# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        top, bottom = 0, m
        left, right = 0, n
        matrix = [[-1] * n for _ in range(m)]

        cur = head
        while cur:
            # fill the top row
            for c in range(left, right):
                if not cur:
                    return matrix
                matrix[top][c] = cur.val
                cur = cur.next
            top = top + 1

            # fill the right row
            for r in range(top, bottom):
                if not cur:
                    return matrix
                matrix[r][right - 1] = cur.val
                cur = cur.next
            right = right - 1

            if left > right or top > bottom:
                break

            # fill the bottom row
            for c in range(right - 1, left - 1, -1):
                if not cur:
                    return matrix
                matrix[bottom - 1][c] = cur.val
                cur = cur.next
            bottom = bottom - 1

            # fill the left row
            for r in range(bottom - 1, top - 1, -1):
                if not cur:
                    return matrix
                matrix[r][left] = cur.val
                cur = cur.next
            left = left + 1

        return matrix
