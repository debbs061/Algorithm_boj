from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.endOfWord = True

    def findWord(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.endOfWord

    def prune(self, word):
        cur = self
        stack = []

        for ch in word:
            stack.append(cur)
            cur = cur.children[ch]
        cur.endOfWord = False

        for t_node, ch in reversed(list(zip(stack, word))):
            if len(t_node.children[ch].children) > 0:  # has children
                return
            else:
                del t_node.children[ch]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        result, visit = set(), set()
        ROWS, COLS = len(board), len(board[0])

        for word in words:
            root.addWord(word)

        def dfs(x, y, node, word):
            if x < 0 or y < 0 or x == ROWS or y == COLS or (x, y) in visit or board[x][y] not in node.children:
                return
            visit.add((x, y))
            word = word + board[x][y]
            node = node.children[board[x][y]]
            if node.endOfWord:
                result.add(word)
                root.prune(word)

            dfs(x + 1, y, node, word)
            dfs(x - 1, y, node, word)
            dfs(x, y + 1, node, word)
            dfs(x, y - 1, node, word)
            visit.remove((x, y))

        for x in range(ROWS):
            for y in range(COLS):
                dfs(x, y, root, "")
        return list(result)

# 1. build a trie
