class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                return cur.endOfWord
            if word[i] == ".":
                for ch in cur.children:
                    if dfs(i + 1, cur.children[ch]):
                        return True
            else:
                if word[i] not in cur.children:
                    return False
                return dfs(i + 1, cur.children[word[i]])

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
