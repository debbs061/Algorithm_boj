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


class Solution(object):
    def findWords(self, board, words):
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        root = TrieNode()
        for word in words:
            root.addWord(word)

        def dfs(r, c, node, word):
            if (0 > r or 0 > c or r == ROWS or c == COLS or board[r][c] not in node.children or (r, c) in visit):
                return
            visit.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
