class Node:
    def __init__(self):
        self.children = {}  # { alphabet : node }
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                newNode = Node()
                cur.children[w] = newNode
                cur = cur.children[w]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            else:
                cur = cur.children[w]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for p in prefix:
            if p not in cur.children:
                return False
            else:
                cur = cur.children[p]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
