from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def prune(self, word):
        cur = self
        stack = []
        for c in word:  # apple
            stack.append(cur)
            cur = cur.children[c]
        cur.endOfWord = False

        for node, c in reversed(list(zip(stack, word))):
            if len(node.children[c].children) > 0:
                return
            else:
                del node.children[c]


class Solution(object):
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        result = set()

        root = TrieNode()
        for word in words:
            root.addWord(word)

        def dfs(r, c, node, word):
            if r == ROWS or c == COLS or r < 0 or c < 0 or board[r][c] not in node.children or (r, c) in visit:
                return
            visit.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                result.add(word)  # apple
                root.prune(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(result)
