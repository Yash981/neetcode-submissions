class TrieNode:
    def __init__(self):
        self.children = Counter()
        self.isEndOfWord = False
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for x in prefix:
            if x not in node.children:
                return False
            node = node.children[x]
        return True
        
        