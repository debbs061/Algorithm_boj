# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.pointer = TreeNode(-1)
        self.visit = False
        self.stack = []

        def recursive(cur):
            if not cur:
                if not self.visit:
                    self.visit = True
                    return self.pointer
                return None
            cur.left = recursive(cur.left)
            self.stack.append(cur)
            cur.right = recursive(cur.right)
            return cur

        cur = root
        recursive(cur)
        self.stack = self.stack[::-1]

    def next(self) -> int:
        nxt = self.stack[-1].val
        self.stack.pop()
        return nxt

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    # Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
