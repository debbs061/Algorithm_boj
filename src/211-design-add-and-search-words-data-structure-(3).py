class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Node(w)
            cur = cur.children[w]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.endOfWord
            if word[i] == ".":
                for child in node.children:
                    if dfs(i + 1, node.children[child]):
                        return True
                return False
            if word[i] in node.children:
                return dfs(i + 1, node.children[word[i]])

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
