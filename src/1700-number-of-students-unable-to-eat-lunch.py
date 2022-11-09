from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.left = self.right = None

    def enqueue(self, val):
        newNode = ListNode(val)

        # Queue is non-empty
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        # Queue is empty
        else:
            self.left = self.right = newNode

    def dequeue(self):
        # Queue is empty
        if not self.left:
            return None

        # Remove left node and return value
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val

    # def print(self):
    #     cur = self.left
    #     while cur:
    #         print(cur.val, '->', end="")
    #         cur = cur.next
    #     print()


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # make queue and stack
        q = Queue()
        for s in students:
            q.enqueue(s)

        # [1,0,1,0]
        stack = sandwiches[::-1]
        print(stack)

        N = len(stack)
        cnt = 0
        while cnt != N:
            if q.left.val == stack[-1]:
                q.dequeue()
                stack.pop()
                cnt = 0
                N = N - 1
            else:
                val = q.dequeue()
                q.enqueue(val)
                cnt += 1

        return N

a = Solution()
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(a.countStudents(students, sandwiches))
