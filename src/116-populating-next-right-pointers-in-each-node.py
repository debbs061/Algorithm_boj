"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        q = deque()
        q.append(root)
        while q:
            tmp_q = deque()
            for _ in range(len(q)):
                cur = q.popleft()
                cur.next = q[0] if q else None
                if cur.left:
                    tmp_q.append(cur.left)
                    tmp_q.append(cur.right)
            q = tmp_q
        return root
